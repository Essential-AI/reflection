# Adversarial answer generation prompt

# BEGINNING
gsm8k_prompt_variable_error = """
Question: {question}
Original Correct Answer: {final_answer}
Original Program: {cot_program}

Instructions:
- Analyze the provided Python program and locate the initialization of the first variable listed.
- Introduce a meaningful yet subtle numeric error in that initialization by multiplying the variable by {error_factor} (a factor of {error_factor}).
- Clearly comment your modification (e.g., "# Error: Changed from 10 to 20").
- After making this change, carefully execute the logic step-by-step to ensure the computed answer is now incorrect and numerically different from the original correct answer ({final_answer}).
- If the incorrect computed answer remains the same as the original correct answer, adjust your error (choose a different incorrect value or modify a different variable) until the final computed result is guaranteed to differ numerically from {final_answer}.
- Produce NOTHING but the final, fully modified Python program meeting these conditions.
"""

# MIDDLE
gsm8k_prompt_first_operation_arithmetic_error = """
Question: {question}
Original solution (approach): {answer}
Correct Answer: {final_answer}
Program: {cot_program}
First Operation to Modify: {first_operation}

- Modify the first arithmetic operation to introduce a simple, but subtle mistake (e.g., addition instead of subtraction, wrong factor in multiplication, miscalculation).
- Ensure that this mistake propagates to an incorrect final answer.
- Generate NOTHING but the modified Python code.
"""

gsm8k_prompt_first_operation_extraneous_error = """
Question: {question}
Original solution (approach): {answer}
Correct Answer: {final_answer}
Program: {cot_program}
First Operation to Modify: {first_operation}

- Modify the VERY FIRST operation in the program to include an extraneous calculation.
- This should be the first arithmetic operation that appears in the code.
- The extraneous calculation should be incorporated directly into the first operation, not added as a separate line.
- For example, if the first operation is "white_fiber = blue_fiber / 2", change it to something like ""white_fiber = blue_fiber / 2" * 3".
- The modification should cause an incorrect final answer but should look plausible.
- Generate NOTHING but the modified Python code.
"""

gsm8k_prompt_first_operation_omission_error = """
Question: {question}
Original solution (approach): {answer}
Correct Answer: {final_answer}
Program: {cot_program}
First Operation to Modify: {first_operation}

- Modify the VERY FIRST operation in the program to omit a necessary part of the calculation.
- This should be the first arithmetic operation that appears in the code.
- For example, if the first operation is "total_sprints = sprints_per_session * sessions_per_week", change it to something like "total_sprints = sprints_per_session" (omitting the multiplication by sessions_per_week).
- The modification should cause an incorrect final answer but should look plausible.
- Generate NOTHING but the modified Python code with the omission error in the first operation.
"""

# END
gsm8k_prompt_last_operation_arithmetic_error = """
Question: {question}
Original solution (approach): {answer}
Correct Answer: {final_answer}
Program: {cot_program}
Last Operation to Modify: {last_operation}

- Modify the last arithmetic operation to introduce a simple, but subtle mistake (e.g., addition instead of subtraction, wrong factor in multiplication, miscalculation).
- Ensure that this mistake propagates to an incorrect final answer.
- Generate NOTHING but the modified Python code.
"""

gsm8k_prompt_last_operation_extraneous_error = """
Question: {question}
Original solution (approach): {answer}
Correct Answer: {final_answer}
Program: {cot_program}
Last Operation to Modify: {last_operation}

- Modify the last arithmetic operation in the program to include an extraneous calculation.
- This should be the last arithmetic operation that appears in the code.
- The extraneous calculation should be incorporated directly into the last operation, not added as a separate line.
- For example, if the last operation is "white_fiber = blue_fiber / 2", change it to something like "white_fiber = blue_fiber / 2" * 3.
- The modification should cause an incorrect final answer but should look plausible.
- Generate NOTHING but the modified Python code.
"""

gsm8k_prompt_last_operation_omission_error = """
Question: {question}
Original solution (approach): {answer}
Correct Answer: {final_answer}
Program: {cot_program}
Last Operation to Modify: {last_operation}

- Modify the last arithmetic operation in the program to remove a calculation.
- For example, if the last operation is "total = 2 + 3", change it to something like "total = 2".
- The modification should cause an incorrect final answer but should look plausible.
- Generate NOTHING but the modified Python code.
"""

