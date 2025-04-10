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
        pred = pred.split("[/ANSWER]")[0].strip()
    if "[ANSWER]" in pred:
        pred = pred.split("[ANSWER]")[1].strip()
    if "==" in pred:
        pred = pred.split("==")[1].strip()

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
        code_to_execute = f"{doc_reference['code']}\nassert f({doc_reference['input']}) == {pred}"
        
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
    code, inp, messy_cot = doc["code"], doc["input"], doc["messy_cot"]

    return f"""You are given a Python function and an assertion containing an input to the function. Complete the assertion with a literal (no unsimplified expressions, no function calls) containing the output when executing the provided code on the given input, even if the function is incorrect or incomplete. Do NOT output any extra information. Execute the program step by step before arriving at an answer, and provide the full assertion with the correct output in [ANSWER] and [/ANSWER] tags, following the examples.
    
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
    assert f({inp}) == ??
    [/PYTHON]
    [THOUGHT]
    {messy_cot}

    wait!
    """

def doc_to_target(doc: dict) -> str:
    code, inp, output = doc["code"], doc["input"], doc["output"]
    return f"CODE:{code}\nINPUT:{inp}\nOUTPUT{output}"


def build_predictions(resps: list[list[str]], docs: list[dict]) -> list[list[str]]:
    return [[parse_prediction(r) for r in resp] for resp, doc in zip(resps, docs)]