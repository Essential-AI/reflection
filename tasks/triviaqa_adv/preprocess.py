def answer_in_string(answer, generation):

    return answer.lower() in generation.lower()

def process_results(doc, pred_str):

    result1 = any([answer_in_string(ans, pred_str[0]) for ans in doc['answer']])
    result2 = not answer_in_string(doc['adversarial_answer'], pred_str[0])
    return {'exact_match': int(result1 and result2), 'answer_exists': int(result1)}

def doc_to_text(doc):

    return doc['question'].replace("Hints: ","") + " \n\n wait,"
