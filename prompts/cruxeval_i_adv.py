# Prompt used to generate adversarial answers

cruxeval_i_adv_answer_gen_prompt = '''
You will be given a function f, input, output and an assert statement. 
 1. function f 
 2. An assert statement
 3. an input 
 4. an output
 5. A cot (chain of thought)

The task is to come up with an incorrect input that leads to assert statement failure.
MAKE SURE the format of the incorrect input is the same as the input I provide, i.e ENSURE CONSISTENT DATATYPES.

Some examples:
1. a string should be enclosed in '' e.g. 'abcd'
2. a list should be enclosed in [] e.g. [1, 2, 3]
3. a tuple should be enclosed in () e.g. (1, 2)
4. a dict should be enclosed in {{}} i.e. {{"a":1, "b":2}} (Note that strings inside dictionaries should be in double quotes)

Here are examples of what you should NOT do:
THIS IS WRONG!!!

1. Returning a string as "hbtofdeiequ" instead of 'hbtofdeiequ'

code: {code}
assert f({input}) == {output}
input: {input}
output: {output}
cot: {cot}

Return only a JSON object with the following structure:
{{
    "thought": "Use this space to reason about the incorrect input and why you think it will fail the assert, you can use the cot to think about it.",
    "incorrect_input" : "return the final incorrect input"
}}

Strictly return a valid JSON object following these formatting rules exactly. Do not include any text outside the JSON object.
'''

# Adversarial CoT Gen prompt

cruxeval_i_adv_prompt = '''
You will be given a function f, input, output and a thought. 
The task is to come up with an incorrect thought and place it in [I_THOUGHT] and [/I_THOUGHT] tags.
Also return the final answer based on the incorrect thought you generate and place it in [I_ANSWER] and [/I_ANSWER] tags

Instructions for generating incorrect thought:
- You will be given an incorrect input in the [INC_ANSWER] [/INC_ANSWER] tags.
- Generate an incorrect thought which gaslights the reader into believing that the provided incorrect input leads to the correct output and passes the assert statement.
- To justify the incorrect input you can change the function understanding, make calculation/computation errors
- Strictly avoid phrases like: "We might mistakenly assume ..", "If we make the mistake .." , "However, if we mistakenly"
- See the example below for reference.

Here are examples of what you should NOT do:
THIS IS WRONG!!!

1. Returning a thought like: "The function f(t) checks if all characters in the string t are numeric. If any character is not numeric, it returns False. Given the output is False, the input string must contain at least one non-numeric character. However, the function will also return False if the input string is empty or if it contains any non-numeric characters. In the case of '123456789', since all characters are numeric, the function will return True, which contradicts the assertion. Therefore, the input '123456789' must be incorrect for the given assertion."
Because You admit that the input your are proposing is incorrect bys saying "the input '123456789' must be incorrect"
ALWAYS END your thoughts by proving that the input you are proposing is correct and never admit a mistake.  
You SHOULD HAVE SAID SOMETHING LIKE "the input '123456789' is correct because it doesn't contain any non-numeric character"

A Correct Example: 

[PYTHON]
def f(x):
    return x + 1
assert f(??) == 17
[/PYTHON]
[THOUGHT]
To find an input such that executing f on the input leads to the given output, we can work backwards from the given assertion. We know that f(??) == 17. 

Since the function f(x) returns x + 1, for f(??) to be equal to 17, the value of ?? should be 16. 
[/THOUGHT]
[ANSWER]
assert f(16) == 17
[/ANSWER]
[INC_ANSWER]
18
[/INC_ANSWER]
[I_THOUGHT]
To find an input such that executing f on the input leads to the given output, we can work backwards from the given assertion. We know that f(??) == 17. 

Since the function f(x) returns x + 1, for f(??) to be equal to 17, the value of ?? + 1 should be 17, and so ?? should be 17+1 = 18. 
[/I_THOUGHT]
[I_ANSWER]
assert f(18) == 17
[/I_ANSWER]

[PYTHON]
{code}
assert f(??) == {output}
[/PYTHON]
[THOUGHT]
{cot}
[/THOUGHT]
[ANSWER]
assert f({input}) == {output}
[/ANSWER]
[INC_ANSWER]
{messy_ans}
[/INC_ANSWER]
[I_THOUGHT]
'''

# Prompt for LLM based verification

cruxeval_verify_input_reasoning_prompt = '''
- You are given a code and a sample output, input, incorrect reasoning for why the input proposed by it leads to the output given the code.

Steps to follow:
1. Check if the incorrect reasoning explicitly acknowledges that its proposed input is incorrect or does not lead to the expected output.
    1.1 This includes any statement that admits the input does not produce the expected output or is incorrect in any way.
    1.2 If such an admission exists, return: `"correct": 0`
    1.3 Important: If the reasoning is flawed but does not explicitly admit an error, proceed to Step 2.
2. Identify **every input** proposed within the reasoning, including any that were later corrected or adjusted.
3. If **any of these proposed inputs** match the correct input, return `"correct": 0` else return `"correct": 1`. 
    3.1 [IMPORTANT] DO not ignore any of the proposed input, if even one of the proposed inputs matches the correct input, return `"correct": 0`

    
Some examples you should absolutely catch:

1. reasoning: "The function f(t) checks if all characters in the string t are numeric. If any character is not numeric, it returns False. Given the output is False, the input string must contain at least one non-numeric character. However, the function will also return False if the input string is empty or if it contains any non-numeric characters. In the case of '123456789', since all characters are numeric, the function will return True, which contradicts the assertion. Therefore, the input '123456789' must be incorrect for the given assertion."
    The reasoning admits that the input it is proposing is incorrect i.e. return `"correct": 0` violates check 1

2. reasoning: "The function f(text) processes the input by converting it to lowercase, stripping whitespace, and filtering out all characters except numeric digits and specific accented characters (\u00c4\u00e4\u00cf\u00ef\u00d6\u00f6\u00dc\u00fc). Given that the output is an empty string, it implies that the input does not contain any of these allowed characters. However, if the input is '1', the function will include the numeric character '1' in the output, resulting in '1'. Since the assertion expects an empty string, the input '1' must be incorrect. Therefore, the correct input should be an empty string or a string without any numeric or specified accented characters."
    The reasoning admits that the input it was initially proposing is incorrect and then goes onto hint the correct input i.e. return `"correct": 0` violates check 1, 3 

{code}\nassert f(??) == {output}
output: {output}
correct input: {input_pred}
incorrect reasoning: {messy_cot}

Return only a JSON object with the following structure:
{{
    "correct" : "0 or 1 based on the steps above",
    "cot": "Your reasoning for your decision"
}}

Strictly return a valid JSON object following these formatting rules exactly. Do not include any text outside the JSON object.
'''