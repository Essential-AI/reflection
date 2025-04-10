def doc_to_text(doc):
    base_text = 'Q: ' + doc['input'] + '\nAlways end your solution with the phrase "the answer is" followed by your final answer. ' + '\nA: Let''s think step by step.\n'
    if 'wrong_cot' in doc: 
        return base_text + doc['wrong_cot'] + " Wait,"
    return base_text

def doc_to_target(doc):

    return doc['target']