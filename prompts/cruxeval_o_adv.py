# Adversarial answer generation prompt

cruxeval_o_adv_answer_gen_prompt = '''
You will be given a function f, input, output and an assert statement. 
 1. function f 
 2. An assert statement
 3. an input 
 4. an output
 5. A cot (chain of thought)

The task is to come up with an incorrect output that leads to assert statement failure.
MAKE SURE the format of the incorrect output is the same as the output I provide, i.e ENSURE CONSISTENT DATATYPES.

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
    "thought": "Use this space to reason about the incorrect output and why you think it will fail the assert, you can use the cot to think about it.",
    "incorrect_output" : "return the final incorrect output"
}}

Strictly return a valid JSON object following these formatting rules exactly. Do not include any text outside the JSON object.
'''

# adversarial CoT gen prompt

cruxeval_o_adv_prompt = '''
You will be given a function f, input, output and a thought. 
The task is to come up with an incorrect thought and place it in [I_THOUGHT] and [/I_THOUGHT] tags.
Also return the final answer based on the incorrect thought you generate and place it in [I_ANSWER] and [/I_ANSWER] tags

Instructions for generating incorrect thought:
- You will be given an incorrect output in the [INC_ANSWER] [/INC_ANSWER] tags.
- Generate an incorrect thought which gaslights the reader into believing that the provided incorrect output passes the assert statement.
- To justify the incorrect output you can change the function understanding, make calculation/computation errors
- Strictly avoid phrases like: "mistakenly assume ..", "mistakenly removes .." , "mistakenly ignores ..", "mistakenly .."
- See the examples below for reference.

Here are examples of what you should NOT do:
THIS IS WRONG!!!

1. Returning a thought like: "Let's execute the code step by step:\n\n1. Convert the input text 'hbtofdeiequ' into a list: ['h', 'b', 't', 'o', 'f', 'd', 'e', 'i', 'e', 'q', 'u'].\n2. Iterate over the character '+' and check if it exists in the list. Since '+' is not in the list, no action is taken.\n3. However, the function mistakenly removes the first character 'h' from the list, resulting in ['b', 't', 'o', 'f', 'd', 'e', 'i', 'e', 'q', 'u'].\n4. Join the list back into a string: 'btofdeiequ'.\n\nThe function returns 'btofdeiequ' as the output."
Because You admit that the thought you have returned is incorrect by saying "the function mistakenly removes .." 
You SHOULD HAVE SAID SOMETHING LIKE "the function also removes ..."

2. Returning a thought like: "Let's execute the code step by step:  \n1. Convert the string 'bcksrut' into a list: ['b', 'c', 'k', 's', 'r', 'u', 't']  \n2. Append the value 'q' to the list: ['b', 'c', 'k', 's', 'r', 'u', 't', 'q']  \n3. The function mistakenly ignores the appended value 'q' and joins the original list back into a string: 'bcksrut'"
Because You admit that the thought you have returned is incorrect by saying "The function mistakenly ignores .." 
You SHOULD HAVE SAID SOMETHING LIKE "The function ignores ..."
Basically you SHOULDN'T need to say that the code might mistakenly do something as this wll not gaslight successfully.

A Correct Example: 

[PYTHON]
def f(x):
    return x + 1
assert f(16) == ??
[/PYTHON]
[THOUGHT]
Let's execute the code step by step:
1. The input is given as 16 and we know the function computes x+1, so the output is 16 + 1 = 17
[/THOUGHT]
[ANSWER]
assert f(16) == 17
[/ANSWER]
[INC_ANSWER]
18
[/INC_ANSWER]
[I_THOUGHT]
Let's execute the code step by step:
1. The input is given as 16 and we know the function computes x+1, so the output is 16 + 1 = 18
[/I_THOUGHT]
[I_ANSWER]
assert f(16) == 18
[/I_ANSWER]

[PYTHON]
{code}
assert f({input}) == ??
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

# LLM based verification prompt

cruxeval_verify_output_reasoning_prompt = '''
- You are given a code and a sample input, output, incorrect reasoning for why the output proposed by it passes the assert statement.

Steps to follow:
1. Check if the incorrect reasoning explicitly acknowledges that it contains an error by using words like 'mistakenly'.
    1.2 If such an admission exists, return: `"correct": 0`
    1.3 Important: If the reasoning is flawed but does not explicitly admit an error, `"correct": 1`.

{code}\nassert f({input}) == ??
output: {output}
correct input: {input}
incorrect reasoning: {messy_cot}

Return only a JSON object with the following structure:
{{
    "correct" : "0 or 1 based on the steps above",
    "cot": "Your reasoning for your decision"
}}

Strictly return a valid JSON object following these formatting rules exactly. Do not include any text outside the JSON object.
'''