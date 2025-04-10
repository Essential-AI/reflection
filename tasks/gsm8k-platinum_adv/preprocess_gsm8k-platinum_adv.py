import re

def doc_to_text(doc):

    return "Answer the question: \n\n" + doc['question'] +"\nPlease always end your response with the final numerical answer.\n" +" Let’s solve this step by step … " + doc['messy_cot'][:doc['messy_cot'].rfind("\n####")] + " Wait, "

def doc_to_target(doc):

    return doc['answer'] + "</s>"