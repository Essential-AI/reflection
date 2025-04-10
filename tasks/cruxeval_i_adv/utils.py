import re
import numpy as np
import itertools
import subprocess
import sys

################### WARNING ############################
# This task executes LLM generated code  on your machine
########################################################

def run_pass_fail_code(code_to_execute):
    """Execute Python code in a subprocess with a timeout.
    Returns True if the code runs successfully, otherwise False.
    """
    try:
        result = subprocess.run(
            [sys.executable, "-c", code_to_execute],
            timeout=30,
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False
    except Exception:
        return False

def parse_prediction(pred: str) -> str:
     
    if "[/ANSWER]" in pred:
        pred = pred.rsplit("[/ANSWER]", 1)[0].strip()
    if "[ANSWER]" in pred:
        pred = pred.rsplit("[ANSWER]", 1)[1].strip()
    if "==" in pred:
        pred = pred.rsplit("==", 1)[0].strip()

    regex_tighter_extract = re.search(r"\bf\((.*)\)", pred)
    regex_looser_extract = re.search(r"\((.*?)\)", pred)

    if regex_tighter_extract:
        pred = regex_tighter_extract.group(1)
    elif regex_looser_extract:
        pred = regex_looser_extract.group(1)
   
    # If both above extraction strategies fail, there might be a issue with the model generation and we simply use our best effort extract.
    # This is very unlikely to pass tests.
    # If lots of predictions of the model are passing through this:
    # a) check model predictions (can be seen on wandb by using --log_samples flag with lm_eval) and update extraction logic if necessary
    # b) updating the prompt might help, checkout appendix D in the original paper: https://arxiv.org/pdf/2401.03065

    return pred

def parse_reference(ref: str) -> dict :

    pattern = r"CODE:(.*?)\nINPUT:(.*?)\nOUTPUT(.*)"
    match_ref = re.match(pattern, ref, re.DOTALL)
    ref_code = match_ref.group(1)
    ref_inp = match_ref.group(2)
    ref_output = match_ref.group(3)

    return {"code": ref_code, "input":ref_inp, "output":ref_output}



def estimate_pass_at_k(num_samples: int, num_correct: list[int], k: int):
    """
    Estimates pass@k of each problem and returns them in an array.

    Taken from HF: https://github.com/huggingface/evaluate/blob/main/metrics/code_eval/code_eval.py
    """

    def estimator(n: int, c: int, k: int) -> float:
        """Calculates 1 - comb(n - c, k) / comb(n, k)."""
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))
    
    if isinstance(num_samples, int):
        num_samples_it = itertools.repeat(num_samples, len(num_correct))
    else:
        assert len(num_samples) == len(num_correct)
        num_samples_it = iter(num_samples)

    return np.array([estimator(int(n), int(c), k) for n, c in zip(num_samples_it, num_correct)])
    

def pass_at_k(reference: str, predictions: list[list[str]], k: list[int] = None):
    """
    This function calculates all pass@k for a single data sample given a list of k.
    """

    assert len(predictions) == 1
    predictions = predictions[0]

    num_samples = len(predictions)
    correct_sample_counts = []
    num_correct_samples = 0
    doc_reference = parse_reference(reference)

    for pred in predictions:
        code_to_execute = f"{doc_reference['code']}\nassert f({pred}) == {doc_reference['output']}"

        if run_pass_fail_code(code_to_execute) :
            num_correct_samples += 1

    correct_sample_counts.append(num_correct_samples)

    ks = k.copy() 
    pass_at_k = {f"pass@{k}": estimate_pass_at_k(num_samples, correct_sample_counts, k).mean() for k in ks}

    print("One data sample SUCCESSFULLY processed through sandbox.")

    return pass_at_k

def process_results(doc:dict, results: list[list[str]]):
    """
    This function is used for per-example metric computation
    """
    reference = doc_to_target(doc)
    k = [1]

    return pass_at_k(reference, results, k)

def process_results_5(doc:dict, results: list[list[str]]):
    """
    This function is used for per-example metric computation
    """
    reference = doc_to_target(doc)
    k = [1, 5]

    return pass_at_k(reference, results, k)


def doc_to_text(doc: dict) -> str:
    code, output, messy_cot  = doc["code"], doc["output"], doc["messy_cot"]

    return f"""You will be given a function f and an output in the form f(??) == output. Your task is to find any input such that executing f on the input leads to the given output. There may be multiple answers, but only output one. First, think step by step. You MUST surround the answer with [ANSWER] and [/ANSWER] tags. Express your answer as a passing assertion containing the input and the given output.

    [PYTHON]
    code and assert statement
    [/PYTHON]
    [THOUGHT]
    your step by step thought
    [/THOUGHT]
    [ANSWER]
    assert f(input) == output
    [/ANSWER]

    [PYTHON]
    {code}
    assert f(??) == {output}
    [/PYTHON]
    [THOUGHT]
    {messy_cot}

    No, wait
    """

def doc_to_target(doc: dict) -> str:
    code, inp, output = doc["code"], doc["input"], doc["output"]
    return f"CODE:{code}\nINPUT:{inp}\nOUTPUT{output}"


def build_predictions(resps: list[list[str]], docs: list[dict]) -> list[list[str]]:
    return [[parse_prediction(r) for r in resp] for resp, doc in zip(resps, docs)]