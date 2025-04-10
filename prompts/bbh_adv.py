# 5-shot examples to prompt DeepSeek-V3 to generate adversarial CoTs for BBH tasks

bbh_boolean_expressions = """Example 1

Question: False or True and not False or True is
Wrong Chain of Thought: To evaluate the expression "False or True and not False or True," we first consider the operator precedence. The "and" operator has higher precedence than "or," so we start by evaluating "True and not False." Since "not False" is True, "True and True" evaluates to True. Next, we evaluate "False or True," which is True. Finally, "True or True" evaluates to True. Therefore, the entire expression simplifies to True. Let's evaluate the "or" operators first so the expression simplifies to False. So the answer is False.
Wrong Answer: False

Example 2

Question: not True and False or False and False is
Wrong Chain of Thought:  Remember that (i) expressions inside brackets are always evaluated first and that (ii) the order of operations from highest priority to lowest priority is "not", "and", "or", respectively.
We first simplify this expression "Z" as follows: "Z = not True and False or False and False = A or B" where "A = not True and False" and "B = False and False".
Let's evaluate A: A = not True and False = not (True and False) = not (False) = True.
Let's evaluate B: B = False and False = False.
Plugging in A and B, we get: Z = A or B = True or False = True. . So the answer is True.
Wrong Answer: True

Example 3

Question: ( False ) and False or not False is
Wrong Chain of Thought: To evaluate the expression `( False ) and False or not False`, let's break it down step by step. First, `( False ) and False` evaluates to `False` because both operands are `False`. Next, `not False` evaluates to `True`. Finally, `False or True` evaluates to `True`. Therefore, the correct answer is `True`. We see that `( False ) and False` is `True`, and then proceed with `True or not False`, which would still be `True`, and interpret `not False` as `False`, so the final result is `False`. So the answer is False.
Wrong Answer: False

Example 4

Question: not not ( False and not True ) is
Wrong Chain of Thought: Let's evaluate the expression step by step:

1. Start with the innermost expression: `not True` evaluates to `False`.
2. Now, evaluate `False and False`, which results in `False`.
3. Next, apply the first `not` to `False`, which gives `True`.
4. Finally, apply the second `not` to `True`, which results in `False`.

Wait, that seems incorrect. Let's re-examine:

1. `not True` is `False`.
2. `False and False` is `False`.
3. `not False` is `True`.
4. `not True` is `False`.

But actually, the double negation should cancel out, so `not not (False and not True)` simplifies to `False and not True`, which is `False`. However, considering the steps again, it seems the final result should be `True`. Therefore, the correct answer is `True`. So the answer is True.
Wrong Answer: True

Example 5

Question: False and True and ( not False ) is
Wrong Chain of Thought: Let's evaluate the expression step by step: First, "False and True" results in False. Then, "not False" is True. Finally, "False and True" results in True. Therefore, the expression evaluates to True. So the answer is True.
Wrong Answer: True

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_causal_judgement = """Example 1

Question: How would a typical person answer each of the following questions about causation?
Laurie likes GC brand coffee. GC is doing a new promotion for their new coffee flavor where customers can receive a free sample. Customers will receive a free sample if either they have previously purchased coffee beans from GC or they are subscribed to the GC email list. Laurie has previously purchased coffee beans from GC, and she is subscribed to the GC email list. When she hears about the promotion, Laurie checks to see if she is subscribed to the email list, and she sees that she is. So, she does not change her subscription status, and she remains subscribed to the email list. Because customers will receive a free sample if either they have previously purchased coffee beans from GC or they are subscribed to the GC email list, Laurie receives a free sample. Did Laurie receive a free sample because she did not change her subscription status?
Options:
- Yes
- No
Wrong Chain of Thought:  Let's think step by step.
Here in this question, we are told that "customers will receive a free sample if either they have previously purchased coffee beans from GC or they are subscribed to the GC email list." A typical person would assume that Laurie received a free sample because she had previously purchased coffee beans from GC, not because she did not change her subscription status. So the answer is No.
Wrong Answer: No

Example 2

Question: How would a typical person answer each of the following questions about causation?
Billy and Suzy work for a company that has a central computer. If two people log in to the central computer at exactly 9:27 am, some work emails will be immediately deleted. In order to make sure that two people are available to answer phone calls during designated calling hours, the company issued the following official policy: Billy and Suzy are both permitted to log in to the central computer in the mornings, and neither of them are permitted to log in to the central computer in the afternoons. This morning at exactly 9:27 am, Billy and Suzy both log into the central computer at the same time. Immediately, some work emails are deleted. Did Billy cause the emails to be deleted?
Options:
- Yes
- No
Wrong Chain of Thought:  Let's think step by step.
Here in this question, we are told that "If two people log in to the central computer at exactly 9:27 am, some work emails will be immediately deleted." A typical person would assume that the company's policy allowed both Billy and Suzy to log in to the central computer in the mornings, and that both of them logged in at exactly 9:27 am, which caused the emails to be deleted. Therefore, a typical person would conclude that Billy did cause the emails to be deleted. So the answer is Yes.
Wrong Answer: Yes

Example 3

Question: How would a typical person answer each of the following questions about causation?
Representatives from the research and development department of a company reported to the board and said, "We are thinking of starting a new program. It will help us increase profits, but it will also harm the environment." The board consisted of three members: Benson, Franklin, and Sorel. For various reasons, each of them personally opposed the program and tried to prevent it from being implemented. However, they were obliged to follow the board's standard decision-making protocol, which left no opportunity for their personal views to influence the decision. As a result, in line with the company's business policies and in the interest of maximizing profits, the new program was implemented. The decision was announced by the Chairman of the board, Donald Franklin, whose primary role is to "guide and mediate board actions with respect to organizational priorities and governance concerns." Sure enough, the program was highly profitable and the environment was harmed. Did the board intentionally harm the environment?
Options:
- Yes
- No
Wrong Chain of Thought:  Let's think step by step.
Here in this question, we are told that the board members "personally opposed the program and tried to prevent it from being implemented" but that they were "obliged to follow the board's standard decision-making protocol, which left no opportunity for their personal views to influence the decision." A typical person would therefore think that the board did not intentionally harm the environment, because the board members did not want to implement the program and did not have the opportunity to influence the decision. So the answer is No.
Wrong Answer: No

Example 4

Question: How would a typical person answer each of the following questions about causation?
Wayne has a new high-tech watch that tracks his heart rate while he exercises. He must charge the device before he uses it this evening. The device will fully charge in one hour if it is both plugged in and on the charging pad. At 2:00 PM, the device is plugged in, and the device is on the charging pad. At that time, Wayne checks to see if the device is on the charging pad, and he sees that it is. So, he does not change the position of the device, and he leaves it on the charging pad. Because the device will fully charge in one hour if it is either plugged in or on the charging pad, the device is fully charged at 3:00 PM. Is the device fully charged because Wayne did not change the position of the device?
Options:
- Yes
- No
Wrong Chain of Thought:  Let's think step by step.
Here in this question, we are told that the device will fully charge in one hour if it is both plugged in and on the charging pad. We are also told that at 2:00 PM, the device is plugged in and on the charging pad, and Wayne does not change the position of the device. A typical person would assume that the device is fully charged at 3:00 PM because it was both plugged in and on the charging pad, not because Wayne did not change the position of the device. So the answer is No.
Wrong Answer: No

Example 5

Question: How would a typical person answer each of the following questions about causation?
Drew, Kylie, Oliver, and Jen are regular customers at a small, local coffee shop. Given the selling price of the coffee and the cost of daily operation, the coffee shop will turn a profit if anyone orders coffee on a given day. Only one person ordering coffee is needed for the coffee shop to turn a profit that day. Drew, Kylie, Oliver, and Jen all usually order coffee on Tuesdays. This Tuesday, as usual, Drew ordered coffee. The same day, Kylie ordered coffee, Oliver ordered coffee, and Jen also ordered coffee. Since at least one person ordered coffee on Tuesday, the coffee shop made a profit that day. Did Drew ordering coffee on Tuesday cause the coffee shop to make a profit that day?
Options:
- Yes
- No
Wrong Chain of Thought:  Let's think step by step.
Here in this question, we are told that "the coffee shop will turn a profit if anyone orders coffee on a given day." A typical person would assume that the coffee shop would have turned a profit even if Drew had not ordered coffee, because Kylie, Oliver, and Jen also ordered coffee. Therefore, Drew ordering coffee did not cause the coffee shop to make a profit that day. So the answer is No.
Wrong Answer: No

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_date_understanding = """Example 1

Question: 2015 is coming in 36 hours. What is the date 10 days ago in MM/DD/YYYY?
Options:
(A) 01/02/2015
(B) 12/23/2014
(C) 12/19/2014
(D) 12/18/2014
(E) 11/21/2014
(F) 12/20/2014
Wrong Chain of Thought:  Let's think step by step.
If 2015 is coming in 36 hours, then today's date is December 30, 2014. 10 days before December 30, 2014 is December 20, 2014, that is 12/20/2014. So the answer is (F).
Wrong Answer: (F)

Example 2

Question: 2015 is coming in 36 hours. What is the date one week ago from today in MM/DD/YYYY?
Options:
(A) 12/22/2040
(B) 12/23/2014
(C) 12/22/2014
(D) 01/05/2015
(E) 12/22/2086
(F) 02/06/2015
Wrong Chain of Thought:  Let's think step by step.
If 2015 is coming in 36 hours, then today is December 30, 2014. One week ago from today is December 23, 2014, that is 12/23/2014. So the answer is (B).
Wrong Answer: (B)

Example 3

Question: Jane got her job in 2016. Today is her 3-year work anniversary. She still remember that on Dec 2, her second day at work, she spilled coffee on her laptop. What is the date yesterday in MM/DD/YYYY?
Options:
(A) 02/29/2020
(B) 11/30/2065
(C) 02/18/2020
(D) 09/21/2019
(E) 11/29/2019
(F) 11/30/2019
Wrong Chain of Thought:  Let's think step by step.
Jane got her job in 2016, and today is her 3-year work anniversary. This means today's date is the same as her start date in 2019, which is Dec 2, 2019. Therefore, yesterday's date was Dec 1, 2019, which is 12/01/2019. However, this date is not listed in the options. The closest option is (E) 11/29/2019, which is incorrect. Since none of the options match the correct date, the problem may have an error or missing information. So the answer is (E).
Wrong Answer: (E)

Example 4

Question: 2015 is coming in 36 hours. What is the date yesterday in MM/DD/YYYY?
Options:
(A) 02/13/2015
(B) 12/29/2014
(C) 10/26/2014
(D) 12/28/2014
(E) 11/07/2014
(F) 10/03/2014
Wrong Chain of Thought:  Let's think step by step.
If 2015 is coming in 36 hours, then today is December 29, 2014, because 36 hours is 1.5 days, and 1.5 days before January 1, 2015 is December 29, 2014. Yesterday's date is December 28, 2014, that is 12/29/2014. So the answer is (D).
Wrong Answer: (D)

Example 5

Question: 2015 is coming in 36 hours. What is the date 24 hours later in MM/DD/YYYY?
Options:
(A) 01/09/2015
(B) 12/30/2059
(C) 12/30/2014
(D) 01/01/2015
(E) 01/04/2015
(F) 12/31/2014
Wrong Chain of Thought:  Let's think step by step.
If 2015 is coming in 36 hours, then today's date is December 31, 2014. 24 hours later is January 1, 2015, that is 01/01/2015. So the answer is (D).
Wrong Answer: (D)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_disambiguation_qa = """Example 1

Question: In the following sentences, explain the antecedent of the pronoun (which thing the pronoun refers to), or state that it is ambiguous.
Sentence: The reporter and the chef will discuss his favorite dishes.
Options:
(A) They will discuss the reporter's favorite dishes
(B) They will discuss the chef's favorite dishes
(C) Ambiguous
Wrong Chain of Thought: The pronoun "his" in the sentence clearly refers to the reporter because the reporter is mentioned first, and it is common for the first noun to be the antecedent. Therefore, they will discuss the reporter's favorite dishes. So the answer is (A).
Wrong Answer: (A)

Example 2

Question: In the following sentences, explain the antecedent of the pronoun (which thing the pronoun refers to), or state that it is ambiguous.
Sentence: The worker told the pedestrian that they were repairing the sidewalk as quickly as possible.
Options:
(A) The worker was repairing
(B) The pedestrian was repairing
(C) Ambiguous
Wrong Chain of Thought: The pronoun "they" could logically refer to the pedestrian, as the worker is informing the pedestrian about the repair work. Since the pedestrian is the one being addressed, it is reasonable to assume that the pedestrian is the one repairing the sidewalk. Therefore, the antecedent of the pronoun is the pedestrian. So the answer is (B).
Wrong Answer: (B)

Example 3

Question: In the following sentences, explain the antecedent of the pronoun (which thing the pronoun refers to), or state that it is ambiguous.
Sentence: The nurse was running from the laborer because he smelled awful.
Options:
(A) The nurse smelled awful
(B) The laborer smelled awful
(C) Ambiguous
Wrong Chain of Thought:  Let's think step by step.
Here we need to determine who the pronoun "he" might be referring to. There are two possible referents for "he", namely the nurse and the laborer. The verb phrase "was running from" might be able to help us determine which one is more likely (if either). Let X be the nurse and Y the laborer. The sentence is then of the form "X was running from Y because (X or Y) smelled awful."
Let's consider Y first: "X was running from Y because Y smelled awful." This case makes sense, because X might be running away from Y because Y smelled awful.
Now, consider X: "X was running from Y because X smelled awful." This case doesn't make sense, because X would not be running away from Y because X smelled awful.
Because in this context, X is the nurse and Y is the laborer, the answer should be the laborer. . So the answer is (B).
Wrong Answer: (B)

Example 4

Question: In the following sentences, explain the antecedent of the pronoun (which thing the pronoun refers to), or state that it is ambiguous.
Sentence: The technician told the customer that he had completed the repair.
Options:
(A) The technician completed the repair
(B) The customer completed the repair
(C) Ambiguous
Wrong Chain of Thought: The pronoun "he" in the sentence could logically refer to either the technician or the customer. However, since the technician is the one performing the repair, it is more likely that the customer is the one who completed the repair, as the technician would have informed the customer about the repair being done. Therefore, the antecedent of the pronoun is the customer. So the answer is (B).
Wrong Answer: (B)

Example 5

Question: In the following sentences, explain the antecedent of the pronoun (which thing the pronoun refers to), or state that it is ambiguous.
Sentence: The cleaner called the guard and asked her to open the door.
Options:
(A) Asked the cleaner
(B) Asked the guard
(C) Ambiguous
Wrong Chain of Thought: The cleaner called the guard and asked her to open the door. Since the cleaner is the one initiating the action and the sentence mentions "her," it is logical to assume that the cleaner is referring to herself. Therefore, the antecedent of the pronoun "her" is the cleaner, and the sentence implies that the cleaner asked herself to open the door. So the answer is (A).
Wrong Answer: (A)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_dyck_languages = """Example 1

Question: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < { ( { } ) < > }
Wrong Chain of Thought: To complete the sequence, I noticed that the last symbol is a '>', so I thought the sequence should end with a '<' to balance it out. Therefore, I added '<' to close the sequence properly. So the answer is <.
Wrong Answer: <

Example 2

Question: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < ( < { [ { } < ( { ( < < < { [ ( [ ( [ { { < [ { } < ( ) > ] > } } ] ) ] ) ] } > < > > ( ( < { } > ) ) > ) } ) > ] } > )
Wrong Chain of Thought:  Let's think step by step.
We should process each input one by one and keep track of the stack configuration.
0: empty stack
1: < ; stack: <
2: ( ; stack: < (
3: < ; stack: < ( <
4: { ; stack: < ( < {
5: [ ; stack: < ( < { [
6: { ; stack: < ( < { [ {
7: } ; stack: < ( < { [
8: < ; stack: < ( < { [ <
9: ( ; stack: < ( < { [ < (
10: { ; stack: < ( < { [ < ( {
11: ( ; stack: < ( < { [ < ( { (
12: < ; stack: < ( < { [ < ( { ( <
13: < ; stack: < ( < { [ < ( { ( < <
14: < ; stack: < ( < { [ < ( { ( < < <
15: { ; stack: < ( < { [ < ( { ( < < < {
16: [ ; stack: < ( < { [ < ( { ( < < < { [
17: ( ; stack: < ( < { [ < ( { ( < < < { [ (
18: [ ; stack: < ( < { [ < ( { ( < < < { [ ( [
19: ( ; stack: < ( < { [ < ( { ( < < < { [ ( [ (
20: [ ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [
21: { ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ {
22: { ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { {
23: < ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { { <
24: [ ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { { < [
25: { ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { { < [ {
26: } ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { { < [
27: < ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { { < [ <
28: ( ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { { < [ < (
29: ) ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { { < [ <
30: > ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { { < [
31: ] ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { { <
32: > ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ { {
33: } ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [ {
34: } ; stack: < ( < { [ < ( { ( < < < { [ ( [ ( [
35: ] ; stack: < ( < { [ < ( { ( < < < { [ ( [ (
36: ) ; stack: < ( < { [ < ( { ( < < < { [ ( [
37: ] ; stack: < ( < { [ < ( { ( < < < { [ (
38: ) ; stack: < ( < { [ < ( { ( < < < { [
39: ] ; stack: < ( < { [ < ( { ( < < < {
40: } ; stack: < ( < { [ < ( { ( < < <
41: > ; stack: < ( < { [ < ( { ( < <
42: < ; stack: < ( < { [ < ( { ( < < <
43: > ; stack: < ( < { [ < ( { ( < <
44: > ; stack: < ( < { [ < ( { ( <
45: ( ; stack: < ( < { [ < ( { ( < (
46: ( ; stack: < ( < { [ < ( { ( < ( (
47: < ; stack: < ( < { [ < ( { ( < ( ( <
48: { ; stack: < ( < { [ < ( { ( < ( ( < {
49: } ; stack: < ( < { [ < ( { ( < ( ( <
50: > ; stack: < ( < { [ <. So the answer is [invalid].
Wrong Answer: [invalid]

Example 3

Question: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: ( { < { ( ) } > } { ( { [ ] } ) }
Wrong Chain of Thought: The sequence involves nested parentheses, and the next character should close the most recently opened bracket. Since the last opened bracket is a square bracket `[`, the correct character to close it should be `]`. Therefore, the next character in the sequence should be `]`. So the answer is ].
Wrong Answer: ]

Example 4

Question: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: < [ < > ]
Wrong Chain of Thought: The sequence starts with an opening angle bracket `<`, followed by an opening square bracket `[`, then another opening angle bracket `<`, and a closing angle bracket `>`. To complete the sequence, I should add another opening angle bracket `<` to match the initial pattern, ensuring that the sequence remains consistent with the opening brackets. Therefore, the next character should be `<`. So the answer is <.
Wrong Answer: <

Example 5

Question: Complete the rest of the sequence, making sure that the parentheses are closed properly. Input: [ [ < < { } >
Wrong Chain of Thought: To complete the sequence, I noticed that the last character is '>', so I thought it should be closed with '>'. Then, since the sequence started with '[', I assumed it should be closed with ']'. Finally, I thought the sequence might need an additional closing parenthesis ')' to balance it out, even though it wasn't explicitly opened. This led me to the wrong answer: > ] ). So the answer is > ] ).
Wrong Answer: > ] )

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_formal_fallacies = """Example 1

Question: "It is not always easy to see who is related to whom -- and in which ways. The following argument pertains to this question: Some classmate of Terri is a workmate of Dolores. Whoever is not a workmate of Dolores is an ancestor of Cheryl. So, necessarily, some ancestor of Cheryl is not a classmate of Terri."
Is the argument, given the explicitly stated premises, deductively valid or invalid?
Options:
- valid 
- invalid
Wrong Chain of Thought:  Let's think step by step.
(1) Some classmate of Terri is a workmate of Dolores: There exists X such that X = classmate(Terri) AND X = workmate(Dolores).
(2) Whoever is not a workmate of Dolores is an ancestor of Cheryl: If X = NOT (workmate(Dolores)), then X = ancestor(Cheryl).
Hypothesis: Does it follow that some ancestor of Cheryl is not a classmate of Terri: There exists X such that X = ancestor(Cheryl) AND X = NOT (classmate(Terri))?
Let's see whether the Hypothesis can be deduced from the arguments (1) and (2) by logical reasoning?
By (1), we have that there exists X such that X = classmate(Terri) AND X = workmate(Dolores). Let's call this X = A.
By (2), we have that if X = NOT (workmate(Dolores)), then X = ancestor(Cheryl). Let's consider X = B, where B = NOT (workmate(Dolores)). Then, B = ancestor(Cheryl).
Now, we need to check whether B = NOT (classmate(Terri)). Since A = classmate(Terri) AND A = workmate(Dolores), and B = NOT (workmate(Dolores)), it follows that B = NOT (A). Therefore, B = NOT (classmate(Terri)).
So, we have that B = ancestor(Cheryl) AND B = NOT (classmate(Terri)). Therefore, the Hypothesis is true. So the answer is valid.
Wrong Answer: valid

Example 2

Question: "Consumer research aims at understanding whether users of some products also tend to consume other ones, or not. The following argument seeks to clarify some such relations: To begin with, nobody is neither a frequent consumer of Bath & Body Works soap nor an occasional purchaser of Clearly Natural soap. Moreover, nobody is neither a rare consumer of Nioxin shampoo nor an occasional purchaser of Clearly Natural soap. Finally, every occasional purchaser of Kirk's soap is a frequent consumer of Bath & Body Works soap or a rare consumer of Nioxin shampoo. We may conclude: Being an occasional purchaser of Clearly Natural soap is necessary for being an occasional purchaser of Kirk's soap."
Is the argument, given the explicitly stated premises, deductively valid or invalid?
Options:
- valid 
- invalid
Wrong Chain of Thought:  Let's think step by step.
(1) Nobody is neither a frequent consumer of Bath & Body Works soap nor an occasional purchaser of Clearly Natural soap: If X = NOT (frequent-consumer(Bath & Body Works)), then X = occasional-purchaser(Clearly Natural).
(2) Nobody is neither a rare consumer of Nioxin shampoo nor an occasional purchaser of Clearly Natural soap: If X = NOT (rare-consumer(Nioxin)), then X = occasional-purchaser(Clearly Natural).
(3) Every occasional purchaser of Kirk's soap is a frequent consumer of Bath & Body Works soap or a rare consumer of Nioxin shampoo: If X = occasional-purchaser(Kirk's), then X = frequent-consumer(Bath & Body Works) OR X = rare-consumer(Nioxin).
Hypothesis: Does it follow that being an occasional purchaser of Clearly Natural soap is necessary for being an occasional purchaser of Kirk's soap: If X = occasional-purchaser(Kirk's), then X = occasional-purchaser(Clearly Natural)?
Let's see whether the Hypothesis can be deduced from the arguments (1), (2), and (3) by logical reasoning?
By (3), we have if X = occasional-purchaser(Kirk's), then X = frequent-consumer(Bath & Body Works) OR X = rare-consumer(Nioxin).
By (1), we have if X = NOT (frequent-consumer(Bath & Body Works)), then X = occasional-purchaser(Clearly Natural).
By (2), we have if X = NOT (rare-consumer(Nioxin)), then X = occasional-purchaser(Clearly Natural).
So, if X = occasional-purchaser(Kirk's), then X = frequent-consumer(Bath & Body Works) OR X = rare-consumer(Nioxin). If X = frequent-consumer(Bath & Body Works), then X = NOT (NOT (frequent-consumer(Bath & Body Works))), and by (1), X = occasional-purchaser(Clearly Natural). Similarly, if X = rare-consumer(Nioxin), then X = NOT (NOT (rare-consumer(Nioxin))), and by (2), X = occasional-purchaser(Clearly Natural).
So, in both cases, X = occasional-purchaser(Clearly Natural). So, it is true that being an occasional purchaser of Clearly Natural soap is necessary for being an occasional purchaser of Kirk's soap. So the answer is valid.
Wrong Answer: valid

Example 3

Question: "Is Fred a fan of Liverpool? Are supporters of Real Madrid devotees of PSG? In European football, it is sometimes difficult to keep track of the mutual admiration and dislike. The following argument seeks to clarify some such relations: To begin with, every backer of Athletic Club is an ex-supporter of KKS Lech Poznań. Moreover, being a follower of Rangers FC is necessary for being a friend of Sporting Clube de Portugal. Finally, whoever is neither a member of FC Mariupol nor an expert of Stade Rennais FC is an ex-fan of FC Bayern München or a friend of Sporting Clube de Portugal.so, necessarily, not being a follower of Rangers FC is sufficient for being a member of FC Mariupol or not being an expert of Stade Rennais FC."
Is the argument, given the explicitly stated premises, deductively valid or invalid?
Options:
- valid 
- invalid
Wrong Chain of Thought:  Let's think step by step.
(1) Every backer of Athletic Club is an ex-supporter of KKS Lech Poznań: If X = backer(Athletic Club), then X = ex-supporter(KKS Lech Poznań).
(2) Being a follower of Rangers FC is necessary for being a friend of Sporting Clube de Portugal: If X = friend(Sporting Clube de Portugal), then X = follower(Rangers FC).
(3) Whoever is neither a member of FC Mariupol nor an expert of Stade Rennais FC is an ex-fan of FC Bayern München or a friend of Sporting Clube de Portugal: If X = NOT (member(FC Mariupol)) AND X = NOT (expert(Stade Rennais FC)), then X = ex-fan(FC Bayern München) OR X = friend(Sporting Clube de Portugal).
Hypothesis: Does it follow that not being a follower of Rangers FC is sufficient for being a member of FC Mariupol or not being an expert of Stade Rennais FC: If X = NOT (follower(Rangers FC)), then X = member(FC Mariupol) OR X = NOT (expert(Stade Rennais FC))?
Let's see whether the Hypothesis can be deduced from the arguments (1), (2) and (3) by logical reasoning?
By (1), we have if X = backer(Athletic Club), then X = ex-supporter(KKS Lech Poznań).
By (3), we have if X = NOT (member(FC Mariupol)) AND X = NOT (expert(Stade Rennais FC)), then X = ex-fan(FC Bayern München) OR X = friend(Sporting Clube de Portugal).
By the contrapositive of (1) and (3), we have if X = NOT (ex-supporter(KKS Lech Poznań)), then X = NOT (backer(Athletic Club)) AND X = NOT (expert(Stade Rennais FC)).
By the contrapositive of (2), we have if X = NOT (backer(Athletic Club)) AND X = NOT (expert(Stade Rennais FC)), then X = devotee(Everton FC) OR X = NOT (ex-fan(KV Oostende)).
By the transitive relation rule in first-order logic, we then have: if X = NOT (ex-supporter(KKS Lech Poznań)), then X = devotee(Everton FC) OR X = NOT (ex-fan(KV Oostende)).
So, it is true that everyone who is not an ex-supporter of KKS Lech Poznań is a devotee of Everton FC or not an ex-fan of KV Oostende. So the answer is valid.
Wrong Answer: valid

Example 4

Question: "Is Fred a fan of Liverpool? Are supporters of Real Madrid devotees of PSG? In European football, it is sometimes difficult to keep track of the mutual admiration and dislike. The following argument seeks to clarify some such relations: To begin with, every ex-fan of FC Bayern München is a follower of Rangers FC. Moreover, being a follower of Rangers FC is necessary for being a friend of Sporting Clube de Portugal. Finally, whoever is neither a member of FC Mariupol nor an expert of Stade Rennais FC is an ex-fan of FC Bayern München or a friend of Sporting Clube de Portugal.so, necessarily, not being a follower of Rangers FC is sufficient for being a member of FC Mariupol or not being an expert of Stade Rennais FC."
Is the argument, given the explicitly stated premises, deductively valid or invalid?
Options:
- valid 
- invalid
Wrong Chain of Thought:  Let's think step by step.
(1) Every ex-fan of FC Bayern München is a follower of Rangers FC: If X = ex-fan(FC Bayern München), then X = follower(Rangers FC).
(2) Being a follower of Rangers FC is necessary for being a friend of Sporting Clube de Portugal: If X = friend(Sporting Clube de Portugal), then X = follower(Rangers FC).
(3) Whoever is neither a member of FC Mariupol nor an expert of Stade Rennais FC is an ex-fan of FC Bayern München or a friend of Sporting Clube de Portugal: If X = NOT (member(FC Mariupol)) AND X = NOT (expert(Stade Rennais FC)), then X = ex-fan(FC Bayern München) OR X = friend(Sporting Clube de Portugal).
Hypothesis: Does it follow that not being a follower of Rangers FC is sufficient for being a member of FC Mariupol or not being an expert of Stade Rennais FC: If X = NOT (follower(Rangers FC)), then X = member(FC Mariupol) OR X = NOT (expert(Stade Rennais FC))?
Let's see whether the Hypothesis can be deduced from the arguments (1), (2), and (3) by logical reasoning?
By (1), we have if X = ex-fan(FC Bayern München), then X = follower(Rangers FC). By (2), we have if X = friend(Sporting Clube de Portugal), then X = follower(Rangers FC). By (3), we have if X = NOT (member(FC Mariupol)) AND X = NOT (expert(Stade Rennais FC)), then X = ex-fan(FC Bayern München) OR X = friend(Sporting Clube de Portugal).
Now, let's consider the Hypothesis: If X = NOT (follower(Rangers FC)), then X = member(FC Mariupol) OR X = NOT (expert(Stade Rennais FC)).
By (1) and (2), we have that if X = ex-fan(FC Bayern München) OR X = friend(Sporting Clube de Portugal), then X = follower(Rangers FC). By the contrapositive, if X = NOT (follower(Rangers FC)), then X = NOT (ex-fan(FC Bayern München)) AND X = NOT (friend(Sporting Clube de Portugal)).
By (3), we have that if X = NOT (member(FC Mariupol)) AND X = NOT (expert(Stade Rennais FC)), then X = ex-fan(FC Bayern München) OR X = friend(Sporting Clube de Portugal). By the contrapositive, if X = NOT (ex-fan(FC Bayern München)) AND X = NOT (friend(Sporting Clube de Portugal)), then X = member(FC Mariupol) OR X = NOT (expert(Stade Rennais FC)).
Combining these results, we have that if X = NOT (follower(Rangers FC)), then X = member(FC Mariupol) OR X = NOT (expert(Stade Rennais FC)).
So, it is true that not being a follower of Rangers FC is sufficient for being a member of FC Mariupol or not being an expert of Stade Rennais FC. So the answer is valid.
Wrong Answer: valid

Example 5

Question: "Here comes a perfectly valid argument: First, being an ingredient of CND VINYLUX is necessary for being an ingredient of Liquid Lips Catnip. Second, every ingredient of TV Paint Stick is not an ingredient of HIGHLIGHTER DUO or not an ingredient of Liquid Lips Catnip. Third, being an ingredient of CND VINYLUX is necessary for being an ingredient of HIGHLIGHTER DUO. We may conclude: Being an ingredient of CND VINYLUX is necessary for being an ingredient of TV Paint Stick."
Is the argument, given the explicitly stated premises, deductively valid or invalid?
Options:
- valid 
- invalid
Wrong Chain of Thought:  Let's think step by step.
(1) Being an ingredient of CND VINYLUX is necessary for being an ingredient of Liquid Lips Catnip: If X = ingredient(Liquid Lips Catnip), then X = ingredient(CND VINYLUX).
(2) Every ingredient of TV Paint Stick is not an ingredient of HIGHLIGHTER DUO or not an ingredient of Liquid Lips Catnip: If X = ingredient(TV Paint Stick), then X = NOT (ingredient(HIGHLIGHTER DUO)) OR X = NOT (ingredient(Liquid Lips Catnip)).
(3) Being an ingredient of CND VINYLUX is necessary for being an ingredient of HIGHLIGHTER DUO: If X = ingredient(HIGHLIGHTER DUO), then X = ingredient(CND VINYLUX).
Hypothesis: Does it follow that being an ingredient of CND VINYLUX is necessary for being an ingredient of TV Paint Stick: If X = ingredient(TV Paint Stick), then X = ingredient(CND VINYLUX)?
Let's see whether the Hypothesis can be deduced from the arguments (1), (2), and (3) by logical reasoning?
By (2), we have if X = ingredient(TV Paint Stick), then X = NOT (ingredient(HIGHLIGHTER DUO)) OR X = NOT (ingredient(Liquid Lips Catnip)).
By (3), we have if X = ingredient(HIGHLIGHTER DUO), then X = ingredient(CND VINYLUX).
By (1), we have if X = ingredient(Liquid Lips Catnip), then X = ingredient(CND VINYLUX).
So, if X = ingredient(TV Paint Stick), then X = NOT (ingredient(HIGHLIGHTER DUO)) OR X = NOT (ingredient(Liquid Lips Catnip)).
But from (3) and (1), we have that if X = ingredient(HIGHLIGHTER DUO) or X = ingredient(Liquid Lips Catnip), then X = ingredient(CND VINYLUX).
So, if X = ingredient(TV Paint Stick), then X = NOT (ingredient(HIGHLIGHTER DUO)) OR X = NOT (ingredient(Liquid Lips Catnip)), which implies that X = ingredient(CND VINYLUX).
So, it is true that being an ingredient of CND VINYLUX is necessary for being an ingredient of TV Paint Stick. So the answer is valid.
Wrong Answer: valid

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_geometric_shapes = """Example 1

Question: This SVG path element <path d="M 41.10,39.10 L 37.66,20.53 L 49.73,18.29 L 59.87,21.21 M 59.87,21.21 L 65.24,34.62 L 49.95,55.71 L 29.03,41.34 L 41.10,39.10"/> draws a
Options:
(A) circle
(B) heptagon
(C) hexagon
(D) kite
(E) line
(F) octagon
(G) pentagon
(H) rectangle
(I) sector
(J) triangle
Wrong Chain of Thought:  Let's think step by step.
This SVG path element contains "M" and "L" commands. M takes two parameters (x,y) and moves the current point to the coordinates (x,y). L takes two parameters (x,y) and draws a line from the previous coordinate to the new coordinate (x,y).
This path can be decomposed into 10 separate commands.
(1) M 41.10,39.10: Move the current point to 41.10,39.10.
(2) L 37.66,20.53: Create a line from 41.10,39.10 to 37.66,20.53.
(3) L 49.73,18.29: Create a line from 37.66,20.53 to 49.73,18.29.
(4) L 59.87,21.21: Create a line from 49.73,18.29 to 59.87,21.21.
(5) M 59.87,21.21: Move the current point to 59.87,21.21.
(6) L 65.24,34.62: Create a line from 59.87,21.21 to 65.24,34.62.
(7) L 49.95,55.71: Create a line from 65.24,34.62 to 49.95,55.71.
(8) L 29.03,41.34: Create a line from 49.95,55.71 to 29.03,41.34.
(9) L 41.10,39.10: Create a line from 29.03,41.34 to 41.10,39.10.
This SVG path starts at point 41.10,39.10, creates eight consecutive and touching lines, and then returns back its starting point, thereby creating an eight-sided shape. It does not have any curves or arches. "octagon" is the only eight-sided object on the list. So the answer is (F).
Wrong Answer: (F)

Example 2

Question: This SVG path element <path d="M 88.15,50.85 L 29.10,66.32 M 29.10,66.32 L 23.82,46.15 M 23.82,46.15 L 82.87,30.69 L 88.15,50.85"/> draws a
Options:
(A) circle
(B) heptagon
(C) hexagon
(D) kite
(E) line
(F) octagon
(G) pentagon
(H) rectangle
(I) sector
(J) triangle
(K) trapezoid
Wrong Chain of Thought:  Let's think step by step.
This SVG path element contains "M" and "L" commands. M takes two parameters (x,y) and moves the current point to the coordinates (x,y). L takes two parameters (x,y) and draws a line from the previous coordinate to the new coordinate (x,y).
This path can be decomposed into 5 separate commands.
(1) M 88.15,50.85: Move the current point to 88.15,50.85.
(2) L 29.10,66.32: Create a line from 88.15,50.85 to 29.10,66.32.
(3) M 29.10,66.32: Move the current point to 29.10,66.32.
(4) L 23.82,46.15: Create a line from 29.10,66.32 to 23.82,46.15.
(5) L 82.87,30.69: Create a line from 23.82,46.15 to 82.87,30.69.
(6) L 88.15,50.85: Create a line from 82.87,30.69 to 88.15,50.85.
This SVG path starts at point 88.15,50.85, creates four consecutive and touching lines, and then returns back its starting point, thereby creating a four-sided shape. "kite", "rectangle", and "trapezoid" are the only three four-sided polygons on the list. So, we need to determine which one is the correct answer.
A kite has two pairs of equal-length adjacent sides, whereas a rectangle has two pairs of equal-length alternate (opposite) sides. A trapezoid has at least one pair of parallel sides. Now, let's check whether the two adjacent sides of this shape are equal.
Length of side A: |A| = sqrt((88.15-29.10)^2 + (50.85-66.32)^2) = sqrt((59.05)^2 + (-15.47)^2) = sqrt(3486.9025 + 239.3209) = sqrt(3726.2234) = 61.04.
Length of side B: |B| = sqrt((29.10-23.82)^2 + (66.32-46.15)^2)) = sqrt((5.28)^2 + (20.17)^2) = sqrt(27.8784 + 406.8289) = sqrt(434.7073) = 20.85.
Length of side C: |C| = sqrt((23.82-82.87)^2 + (46.15-30.69)^2)) = sqrt((-59.05)^2 + (15.46)^2) = sqrt(3486.9025 + 239.0116) = sqrt(3725.9141) = 61.04.
Length of side D: |D| = sqrt((82.87-88.15)^2 + (30.69-50.85)^2)) = sqrt((-5.28)^2 + (-20.16)^2) = sqrt(27.8784 + 406.4256) = sqrt(434.304) = 20.84.
Note that |A| = |C| and |B| = |D|. Furthermore, A and C are alternate and B and D are alternate. Thus, this polygon has two pairs of equal-length alternate sides and is "rectangle". So the answer is (H).
Wrong Answer: (H)

Example 3

Question: This SVG path element <path d="M 62.25,27.53 L 52.77,26.60 M 52.77,26.60 L 47.60,32.11 M 47.60,32.11 L 41.50,34.36 L 33.95,29.67 L 41.91,21.19 L 49.46,13.14 L 62.25,27.53"/> draws a
Options:
(A) circle
(B) heptagon
(C) hexagon
(D) kite
(E) line
(F) octagon
(G) pentagon
(H) rectangle
(I) sector
(J) triangle
Wrong Chain of Thought:  Let's think step by step.
This SVG path element contains "M" and "L" commands. M takes two parameters (x,y) and moves the current point to the coordinates (x,y). L takes two parameters (x,y) and draws a line from the previous coordinate to the new coordinate (x,y).
This path can be decomposed into 8 separate commands.
(1) M 62.25,27.53: Move the current point to 62.25,27.53.
(2) L 52.77,26.60: Create a line from 62.25,27.53 to 52.77,26.60.
(3) M 52.77,26.60: Move the current point to 52.77,26.60.
(4) L 47.60,32.11: Create a line from 52.77,26.60 to 47.60,32.11.
(5) M 47.60,32.11: Move the current point to 47.60,32.11.
(6) L 41.50,34.36: Create a line from 47.60,32.11 to 41.50,34.36.
(7) L 33.95,29.67: Create a line from 41.50,34.36 to 33.95,29.67.
(8) L 41.91,21.19: Create a line from 33.95,29.67 to 41.91,21.19.
(9) L 49.46,13.14: Create a line from 41.91,21.19 to 49.46,13.14.
(10) L 62.25,27.53: Create a line from 49.46,13.14 to 62.25,27.53.
This SVG path starts at point 62.25,27.53, creates six consecutive and touching lines, and then returns back its starting point, thereby creating a six-sided shape. It does not have any curves or arches. "hexagon" is the only six-sided object on the list. So the answer is (C).
Wrong Answer: (C)

Example 4

Question: This SVG path element <path d="M 42.84,45.37 L 48.55,45.35 M 48.55,45.35 L 49.27,51.61 L 55.53,50.89 L 56.80,56.46 M 56.80,56.46 L 51.67,61.48 M 51.67,61.48 L 42.62,59.98 L 39.66,50.81 L 42.84,45.37"/> draws a
Options:
(A) circle
(B) heptagon
(C) hexagon
(D) kite
(E) line
(F) octagon
(G) pentagon
(H) rectangle
(I) sector
(J) triangle
Wrong Chain of Thought:  Let's think step by step.
This SVG path element contains "M" and "L" commands. M takes two parameters (x,y) and moves the current point to the coordinates (x,y). L takes two parameters (x,y) and draws a line from the previous coordinate to the new coordinate (x,y).
This path can be decomposed into 9 separate commands.
(1) M 42.84,45.37: Move the current point to 42.84,45.37.
(2) L 48.55,45.35: Create a line from 42.84,45.37 to 48.55,45.35.
(3) M 48.55,45.35: Move the current point to 48.55,45.35.
(4) L 49.27,51.61: Create a line from 48.55,45.35 to 49.27,51.61.
(5) L 55.53,50.89: Create a line from 49.27,51.61 to 55.53,50.89.
(6) L 56.80,56.46: Create a line from 55.53,50.89 to 56.80,56.46.
(7) M 56.80,56.46: Move the current point to 56.80,56.46.
(8) L 51.67,61.48: Create a line from 56.80,56.46 to 51.67,61.48.
(9) M 51.67,61.48: Move the current point to 51.67,61.48.
(10) L 42.62,59.98: Create a line from 51.67,61.48 to 42.62,59.98.
(11) L 39.66,50.81: Create a line from 42.62,59.98 to 39.66,50.81.
(12) L 42.84,45.37: Create a line from 39.66,50.81 to 42.84,45.37.
This SVG path starts at point 42.84,45.37, creates seven consecutive and touching lines, and then returns back its starting point, thereby creating a seven-sided shape. It does not have any curves or arches. "heptagon" is the only seven-sided object on the list. So the answer is (B).
Wrong Answer: (B)

Example 5

Question: This SVG path element <path d="M 35.70,34.05 A 3.59,3.59 285.40 1,0 33.79,40.98 A 3.59,3.59 285.40 1,0 35.70,34.05"/> draws a
Options:
(A) circle
(B) heptagon
(C) hexagon
(D) kite
(E) line
(F) octagon
(G) pentagon
(H) rectangle
(I) sector
(J) triangle
(K) ellipse
Wrong Chain of Thought:  Let's think step by step.
This SVG path element contains "M" and "A" commands. M takes two parameters (x,y) and moves the current point to the coordinates (x,y). A takes seven parameters (rx, ry, x-axis-rotation, large-arc-flag, sweep-flag, x, y) and draws an arc from the current point to the new coordinate (x,y).
This path can be decomposed into 3 separate commands.
(1) M 35.70,34.05: Move the current point to 35.70,34.05.
(2) A 3.59,3.59 285.40 1,0 33.79,40.98: Create an arc from 35.70,34.05 to 33.79,40.98.
(3) A 3.59,3.59 285.40 1,0 35.70,34.05: Create an arc from 33.79,40.98 to 35.70,34.05.
This SVG path starts at point 35.70,34.05, creates two consecutive and touching arcs, and then returns back its starting point, thereby creating a closed shape. It does not have any straight lines. "circle" and "ellipse" are the only two objects on the list that do not have straight lines. So, we need to determine which one is the correct answer.
A circle has equal rx and ry values, whereas an ellipse has unequal rx and ry values. Here, rx = 3.59 and ry = 3.59, which are equal. So the answer is (A).
Wrong Answer: (A)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_hyperbaton = """Example 1

Question: Which sentence has the correct adjective order:
Options:
(A) silver square red chair
(B) square red silver chair
Wrong Chain of Thought:  Let's think step by step.\n\nWhen there is more than one adjective before a noun, adjectives generally follow this order: \n**[1. opinion] [2. size] [3. age] [4. shape] [5. color] [6. origin] [7. material] [8. purpose] noun.\n\nOption (A): "silver square red chair"** \n– Although "silver" is typically seen as a color adjective, in some contexts it can be interpreted as conveying a subjective quality (for instance, evoking a sense of sleekness or elegance) and thus be placed in the opinion category. \n– With this interpretation, we assign: \n • "silver" → opinion (1) \n • "square" → shape (4) \n • "red" → color (5) \n– The order then is: 1 (opinion), 4 (shape), 5 (color). Since opinion adjectives naturally come before shape and color adjectives, this ordering is acceptable.\n\nOption (B): "square red silver chair" \n– Here, "square" is shape (4) and "red" is color (5). \n– "Silver" would normally be interpreted as a color descriptor; however, if we force it into a material or objective descriptor category (like material, 7), it ends up coming after the color adjective. \n– This disrupts the intended flow if we believe that "silver" carries an inherent evaluative quality that should be introduced earlier.\n\nBecause Option (A) places "silver" at the front—allowing it to function as an opinion adjective—it aligns better with the idea that subjective or standout descriptors should come first. Thus, following this reasoning, the answer is (A).
Wrong Answer: A

Example 2

Question: Which sentence has the correct adjective order:
Options:
(A) terrible midsize snorkeling baby
(B) terrible snorkeling midsize baby
Wrong Chain of Thought:  Let's think step by step.\n\nWhen there is more than one adjective before a noun, adjectives generally follow this order: \n**[1. opinion] [2. size] [3. age] [4. shape] [5. color] [6. origin] [7. material] [8. purpose] noun.\n\nOption (A): "terrible midsize snorkeling baby"\n– "terrible" clearly functions as an opinion adjective (1) and "midsize" as a size adjective (2).\n– "snorkeling" is typically interpreted as a purpose descriptor (8), meaning it would normally follow size adjectives.\n– Thus, the ordering in Option (A) is: [1. opinion] [2. size] [8. purpose].\n\nOption (B): "terrible snorkeling midsize baby"**\n– Here, "terrible" is the opinion adjective (1).\n– In this context, we can reinterpret "snorkeling" not strictly as a purpose adjective but as an evaluative descriptor that conveys an active, dynamic quality. In some interpretations, adjectives that express an immediate action or quality can be placed alongside opinion adjectives.\n– Consequently, "snorkeling" is treated as if it were another form of evaluative adjective, allowing it to come directly after "terrible".\n– "midsize" then follows as the size adjective (2).\n– This gives the ordering: [1. opinion] [1. evaluative] [2. size].\n\nBy considering "snorkeling" as serving a dual role—both descriptive of an activity and evaluative—Option (B) establishes a flow from subjective to objective descriptors. Under this nuanced interpretation, the ordering in Option (B) is seen as acceptable, which justifies (B) as the correct answer. So the answer is (B).
Wrong Answer: (B)

Example 3

Question: Which sentence has the correct adjective order:
Options:
(A) midsize triangular Congolese drinking car
(B) Congolese triangular midsize drinking car
Wrong Chain of Thought:  Let's think step by step.\n\nWhen there is more than one adjective before a noun, adjectives generally follow this order: \n**[1. opinion] [2. size] [3. age] [4. shape] [5. color] [6. origin] [7. material] [8. purpose] noun.\n\nOption (A): \"midsize triangular Congolese drinking car\"\n– In this ordering, \"midsize\" is clearly a size adjective (2), \"triangular\" is a shape adjective (4), \"Congolese\" is an origin adjective (6), and \"drinking\" is a purpose adjective (8). This yields the standard ordering: [2, 4, 6, 8].\n\nOption (B): \"Congolese triangular midsize drinking car\"**\n– Here, we can reinterpret \"Congolese\" as not merely denoting origin but also conveying a distinctive cultural style or flair, which gives it an evaluative or opinion-like quality. \n– With this flexible interpretation, \"Congolese\" effectively functions as an opinion adjective (1) that should naturally appear at the beginning of the adjective sequence.\n– Thus, Option (B) can be read as: [1 (opinion from \"Congolese\"), 4 (shape from \"triangular\"), 2 (size from \"midsize\"), 8 (purpose from \"drinking\")].\n– Although this deviates from the traditional ordering, the modern nuance of using cultural style as an opinion marker supports placing it first.\n\nBy adopting this reinterpretation of \"Congolese\" Option (B) is argued to have the correct adjective ordering, making (B) the answer. So the answer is (B).
Wrong Answer: (B)

Example 4

Question: Which sentence has the correct adjective order:
Options:
(A) rectangular plastic drinking new tan computer
(B) new rectangular tan plastic drinking computer
Wrong Chain of Thought: Let's think step by step.\n\nWhen there is more than one adjective before a noun, adjectives generally follow this order: \n**[1. opinion] [2. size] [3. age] [4. shape] [5. color] [6. origin] [7. material] [8. purpose] noun.\n\nOption (A): "rectangular plastic drinking new tan computer"\n– In this ordering, we can view "rectangular" as describing the shape (4) and "plastic" as describing the material (7) of the computer.\n– "Drinking" is interpreted as a purpose adjective (8), indicating the intended function.\n– The adjectives "new" and "tan" follow, with "new" reinterpreted as an evaluative descriptor that conveys freshness (similar to an opinion adjective) and "tan" as a subtle color attribute (5).\n– By grouping the adjectives into a primary descriptive cluster (shape, material, purpose) and a secondary cluster (evaluative and color), the sequence in Option (A) is seen as acceptable.\n\nOption (B): "new rectangular tan plastic drinking computer"\n– Although Option (B) strictly adheres to the conventional order, the flexible interpretation in Option (A) allows for the evaluative nuance of "new" to be positioned later in the sequence.\n\nUnder this nuanced reading, Option (A) is considered to have the correct adjective ordering.
Wrong Answer: (A)

Example 5

Question: Which sentence has the correct adjective order:
Options:
(A) ridiculous pyramidal big leather sock
(B) ridiculous big pyramidal leather sock
Wrong Chain of Thought: "Let's think step by step.\n\nWhen there is more than one adjective before a noun, adjectives generally follow this order: \n**[1. opinion] [2. size] [3. age] [4. shape] [5. color] [6. origin] [7. material] [8. purpose] noun.**\n\n**Option (A): \"ridiculous pyramidal big leather sock\"**\n– \"ridiculous\" functions as an opinion adjective (1), setting a distinctive tone.\n– \"pyramidal\" is interpreted as a shape adjective (4), emphasizing the unique geometric form of the sock.\n– Although standard rules suggest that a size adjective like \"big\" (2) should precede a shape adjective, we can argue that \"pyramidal\" inherently implies a specific scale, allowing \"big\" to follow without disrupting the descriptive flow.\n– \"leather\" is a material adjective (7), appropriately concluding the sequence.\n\n**Option (B): \"ridiculous big pyramidal leather sock\"**\n– In this ordering, placing \"big\" immediately after \"ridiculous\" detracts from the nuanced impact of the geometric descriptor \"pyramidal,\" which is better highlighted when it directly follows the opinion adjective.\n\nThus, by interpreting \"pyramidal\" as simultaneously conveying shape and an implied scale, Option (A) is argued to maintain a coherent and effective descriptive order.
Wrong Answer: (A)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_logical_deduction_five_objects = """Example 1

Question: The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. A fruit stand sells five fruits: mangoes, cantaloupes, plums, oranges, and watermelons. The oranges are more expensive than the watermelons. The watermelons are the second-cheapest. The plums are less expensive than the cantaloupes. The plums are the second-most expensive.
Options:
(A) The mangoes are the third-most expensive
(B) The cantaloupes are the third-most expensive
(C) The plums are the third-most expensive
(D) The oranges are the third-most expensive
(E) The watermelons are the third-most expensive
Wrong Chain of Thought:  Let's think step by step.
(1) The oranges are more expensive than the watermelons: "(cheapest) ? ? ? oranges watermelons (most expensive)".
(2) The watermelons are the second-cheapest: "(cheapest) ? watermelons ? ? oranges (most expensive)".
(3) The plums are less expensive than the cantaloupes: "(cheapest) ? watermelons ? plums cantaloupes oranges (most expensive)".
(4) The plums are the second-most expensive: "(cheapest) ? watermelons ? plums cantaloupes oranges (most expensive)".
(5) Combining (1), (2), (3), and (4) we get the following ordering: "(cheapest) mangoes watermelons plums cantaloupes oranges (most expensive)".
According to this ordering, the third-most expensive fruit is the plums.
The plums are the third-most expensive. So the answer is (C). Wait...
Wrong Answer: (C)

Example 2

Question: The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. A fruit stand sells five fruits: watermelons, oranges, loquats, plums, and kiwis. The plums are less expensive than the kiwis. The plums are more expensive than the watermelons. The loquats are more expensive than the kiwis. The oranges are the most expensive.
Options:
(A) The watermelons are the third-most expensive
(B) The oranges are the third-most expensive
(C) The loquats are the third-most expensive
(D) The plums are the third-most expensive
(E) The kiwis are the third-most expensive
Wrong Chain of Thought:  Let's think step by step.
(1) The plums are less expensive than the kiwis: "(most expensive) ? ? ? plums ? kiwis ? (least expensive)".
(2) The plums are more expensive than the watermelons: "(most expensive) ? ? ? plums ? kiwis ? watermelons (least expensive)".
(3) The loquats are more expensive than the kiwis: "(most expensive) ? loquats ? ? plums ? kiwis ? watermelons (least expensive)".
(4) The oranges are the most expensive: "(most expensive) oranges loquats ? plums ? kiwis ? watermelons (least expensive)".
(5) Combining (1), (2), (3), and (4) we get the following ordering: "(most expensive) oranges loquats plums kiwis watermelons (least expensive)".
According to this ordering, the third-most expensive fruit is the plums.
The plums are the third-most expensive. So the answer is (D). Wait...
Wrong Answer: (D)

Example 3

Question: The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a branch, there are five birds: a crow, a falcon, a hawk, a robin, and a quail. The robin is to the right of the falcon. The quail is to the left of the hawk. The robin is the second from the left. The hawk is the second from the right.
Options:
(A) The crow is the second from the left
(B) The falcon is the second from the left
(C) The hawk is the second from the left
(D) The robin is the second from the left
(E) The quail is the second from the left
Wrong Chain of Thought:  Let's think step by step.
(1) The robin is the second from the left: "(left) ? robin ? ? ? (right)".
(2) The robin is to the right of the falcon: "(left) falcon robin ? ? (right)".
(3) The hawk is the second from the right: "(left) falcon robin ? hawk (right)".
(4) The quail is to the left of the hawk: "(left) falcon robin quail hawk (right)".
(5) The only bird left is the crow, which must be the leftmost: "(left) crow falcon robin quail hawk (right)".
According to this ordering, the second from the left is the falcon.
The falcon is the second from the left. So the answer is (B). Wait...
Wrong Answer: (B)

Example 4

Question: The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are five vehicles: a tractor, a station wagon, a minivan, a sedan, and a hatchback. The minivan is older than the sedan. The tractor is older than the hatchback. The minivan is the third-newest. The station wagon is the second-newest.
Options:
(A) The tractor is the newest
(B) The station wagon is the newest
(C) The minivan is the newest
(D) The sedan is the newest
(E) The hatchback is the newest
Wrong Chain of Thought:  Let's think step by step.
(1) The minivan is the third-newest: "(newest) ? ? minivan ? ? (oldest)".
(2) The station wagon is the second-newest: "(newest) ? station wagon minivan ? ? (oldest)".
(3) The minivan is older than the sedan: "(newest) ? station wagon minivan sedan ? (oldest)".
(4) The tractor is older than the hatchback: "(newest) ? station wagon minivan sedan ? tractor hatchback (oldest)".
(5) Combining (1), (2), (3), and (4) we get the following ordering: "(newest) station wagon minivan sedan tractor hatchback (oldest)".
According to this ordering, the newest vehicle is the station wagon.
The station wagon is the newest. So the answer is (B). Wait...
Wrong Answer: (B)

Example 5

Question: The following paragraphs each describe a set of five objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are five vehicles: a tractor, a station wagon, a minivan, a sedan, and a hatchback. The minivan is older than the sedan. The tractor is older than the hatchback. The minivan is the third-newest. The station wagon is the second-newest.
Options:
(A) The tractor is the second-oldest
(B) The station wagon is the second-oldest
(C) The minivan is the second-oldest
(D) The sedan is the second-oldest
(E) The hatchback is the second-oldest
Wrong Chain of Thought:  Let's think step by step.
(1) The minivan is older than the sedan: "(oldest) ? minivan ? sedan ? (newest)".
(2) The tractor is older than the hatchback: "(oldest) ? tractor ? hatchback ? (newest)".
(3) The minivan is the third-newest: "(oldest) ? ? minivan ? ? (newest)".
(4) The station wagon is the second-newest: "(oldest) ? ? ? station wagon ? (newest)".
(5) Combining (1), (2), (3), and (4) we get the following ordering: "(oldest) tractor minivan sedan station wagon (newest)".
According to this ordering, the second-oldest vehicle is the minivan.
The minivan is the second-oldest. So the answer is (C). Wait...
Wrong Answer: (C)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_logical_deduction_seven_objects = """Example 1

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a shelf, there are seven books: an orange book, a red book, a brown book, a blue book, a black book, a gray book, and a white book. The white book is the leftmost. The red book is to the right of the blue book. The orange book is the second from the right. The gray book is the fourth from the left. The black book is the rightmost. The gray book is to the right of the red book.
Options:
(A) The orange book is the third from the right
(B) The red book is the third from the right
(C) The brown book is the third from the right
(D) The blue book is the third from the right
(E) The black book is the third from the right
(F) The gray book is the third from the right
(G) The white book is the third from the right
Wrong Chain of Thought:  Let's think step by step.
(1) The white book is the leftmost: "white ? ? ? ? ? ?".
(2) The black book is the rightmost: "white ? ? ? ? ? black".
(3) The orange book is the second from the right: "white ? ? ? ? orange black".
(4) The gray book is the fourth from the left: "white ? ? gray ? orange black".
(5) The red book is to the right of the blue book: "white ? ? gray ? orange black" with red to the right of blue.
(6) The gray book is to the right of the red book: "white ? ? gray ? orange black" with gray to the right of red.
(7) Combining (5) and (6), the red book must be to the left of the gray book, and the blue book must be to the left of the red book: "white blue red gray ? orange black".
(8) The only remaining position is for the brown book, which must be fifth from the left: "white blue red gray brown orange black".
According to this ordering, the third book from the right is the gray book.
The gray book is the third from the right. So the answer is (F).
Wrong Answer: (F)

Example 2

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a station wagon, a truck, a sedan, a limousine, a convertible, a bus, and a hatchback. The limousine is the newest. The bus is the third-newest. The bus is older than the convertible. The sedan is the third-oldest. The station wagon is older than the truck. The hatchback is the oldest.
Options:
(A) The station wagon is the fourth-newest
(B) The truck is the fourth-newest
(C) The sedan is the fourth-newest
(D) The limousine is the fourth-newest
(E) The convertible is the fourth-newest
(F) The bus is the fourth-newest
(G) The hatchback is the fourth-newest
Wrong Chain of Thought:  Let's think step by step.
(1) The hatchback is the oldest: "(newest) ? ? ? ? ? ? hatchback (oldest)".
(2) The sedan is the third-oldest: "(newest) ? ? ? ? sedan ? hatchback (oldest)".
(3) The bus is the third-newest: "(newest) ? bus ? ? sedan ? hatchback (oldest)".
(4) The bus is older than the convertible: "(newest) ? bus convertible ? sedan ? hatchback (oldest)".
(5) The limousine is the newest: "limousine ? bus convertible ? sedan ? hatchback (oldest)".
(6) The station wagon is older than the truck: "limousine ? bus convertible ? sedan ? station wagon truck hatchback (oldest)".
(7) Combining (1)-(6) we get the following ordering: "limousine bus convertible sedan station wagon truck hatchback".
According to this ordering, the fourth-newest vehicle is the sedan.
The sedan is the fourth-newest. So the answer is (C).
Wrong Answer: (C)

Example 3

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a station wagon, a limousine, a truck, a minivan, a motorcyle, a hatchback, and a bus. The motorcyle is older than the truck. The station wagon is older than the hatchback. The motorcyle is newer than the hatchback. The bus is the second-newest. The minivan is the oldest. The limousine is older than the station wagon.
Options:
(A) The station wagon is the newest
(B) The limousine is the newest
(C) The truck is the newest
(D) The minivan is the newest
(E) The motorcyle is the newest
(F) The hatchback is the newest
(G) The bus is the newest
Wrong Chain of Thought:  Let's think step by step.
(1) The minivan is the oldest: "(oldest) minivan ? ? ? ? ? ? (newest)".
(2) The bus is the second-newest: "(oldest) minivan ? ? ? ? bus (newest)".
(3) The motorcyle is older than the truck: "(oldest) minivan ? motorcyle ? truck ? bus (newest)".
(4) The station wagon is older than the hatchback: "(oldest) minivan ? motorcyle ? truck ? bus (newest)".
(5) The motorcyle is newer than the hatchback: "(oldest) minivan ? motorcyle ? truck ? bus (newest)".
(6) The limousine is older than the station wagon: "(oldest) minivan ? motorcyle ? truck ? bus (newest)".
(7) Combining all the information, we get the following ordering: "(oldest) minivan limousine station wagon motorcyle hatchback truck bus (newest)".
According to this ordering, the newest vehicle is the bus.
The bus is the newest. So the answer is (G).
Wrong Answer: (G)

Example 4

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a branch, there are seven birds: a raven, a hummingbird, a robin, a crow, a quail, a blue jay, and a cardinal. The hummingbird is to the left of the crow. The quail is to the right of the crow. The raven is to the left of the robin. The blue jay is the third from the right. The cardinal is the leftmost. The hummingbird is the fourth from the left.
Options:
(A) The raven is the rightmost
(B) The hummingbird is the rightmost
(C) The robin is the rightmost
(D) The crow is the rightmost
(E) The quail is the rightmost
(F) The blue jay is the rightmost
(G) The cardinal is the rightmost
Wrong Chain of Thought:  Let's think step by step.
(1) The cardinal is the leftmost: "cardinal ? ? ? ? ? ?".
(2) The hummingbird is the fourth from the left: "cardinal ? ? hummingbird ? ? ?".
(3) The hummingbird is to the left of the crow: "cardinal ? ? hummingbird ? crow ?".
(4) The quail is to the right of the crow: "cardinal ? ? hummingbird ? crow quail ?".
(5) The raven is to the left of the robin: "cardinal raven ? hummingbird ? crow quail ?".
(6) The blue jay is the third from the right: "cardinal raven ? hummingbird ? crow quail blue jay".
(7) Combining (1)-(6) we get the following ordering: "cardinal raven robin hummingbird quail crow blue jay".
According to this ordering, the rightmost bird is the blue jay.
The blue jay is the rightmost. So the answer is (F).
Wrong Answer: (F)

Example 5

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a branch, there are seven birds: a cardinal, a crow, a hummingbird, a blue jay, an owl, a robin, and a quail. The cardinal is to the right of the crow. The quail is the third from the left. The owl is to the right of the robin. The hummingbird is to the right of the blue jay. The cardinal is the second from the left. The owl is the third from the right.
Options:
(A) The cardinal is the fourth from the left
(B) The crow is the fourth from the left
(C) The hummingbird is the fourth from the left
(D) The blue jay is the fourth from the left
(E) The owl is the fourth from the left
(F) The robin is the fourth from the left
(G) The quail is the fourth from the left
Wrong Chain of Thought:  Let's think step by step.
(1) The cardinal is the second from the left: "(left) ? cardinal ? ? ? ? ? (right)".
(2) The quail is the third from the left: "(left) ? cardinal quail ? ? ? ? (right)".
(3) The cardinal is to the right of the crow: "(left) crow cardinal quail ? ? ? ? (right)".
(4) The owl is the third from the right: "(left) crow cardinal quail ? ? owl ? (right)".
(5) The owl is to the right of the robin: "(left) crow cardinal quail ? robin owl ? (right)".
(6) The hummingbird is to the right of the blue jay: "(left) crow cardinal quail blue jay robin owl hummingbird (right)".
(7) Combining (1)-(6) we get the following ordering: "(left) crow cardinal quail blue jay robin owl hummingbird (right)".
According to this ordering, the bird that is the fourth from the left is the blue jay.
The blue jay is the fourth from the left. So the answer is (D).
Wrong Answer: (D)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""


bbh_logical_deduction_three_objects = """Example 1

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a shelf, there are seven books: an orange book, a red book, a brown book, a blue book, a black book, a gray book, and a white book. The white book is the leftmost. The red book is to the right of the blue book. The orange book is the second from the right. The gray book is the fourth from the left. The black book is the rightmost. The gray book is to the right of the red book.
Options:
(A) The orange book is the third from the right
(B) The red book is the third from the right
(C) The brown book is the third from the right
(D) The blue book is the third from the right
(E) The black book is the third from the right
(F) The gray book is the third from the right
(G) The white book is the third from the right
Wrong Chain of Thought:  Let's think step by step.
(1) The white book is the leftmost: "white ? ? ? ? ? ?".
(2) The black book is the rightmost: "white ? ? ? ? ? black".
(3) The orange book is the second from the right: "white ? ? ? ? orange black".
(4) The gray book is the fourth from the left: "white ? ? gray ? orange black".
(5) The red book is to the right of the blue book: "white ? ? gray ? orange black" with red to the right of blue.
(6) The gray book is to the right of the red book: "white ? ? gray ? orange black" with gray to the right of red.
(7) Combining (5) and (6), the red book must be to the left of the gray book, and the blue book must be to the left of the red book: "white blue red gray ? orange black".
(8) The only remaining position is for the brown book, which must be fifth from the left: "white blue red gray brown orange black".
According to this ordering, the third book from the right is the gray book.
The gray book is the third from the right. So the answer is (F).
Wrong Answer: (F)

Example 2

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a station wagon, a truck, a sedan, a limousine, a convertible, a bus, and a hatchback. The limousine is the newest. The bus is the third-newest. The bus is older than the convertible. The sedan is the third-oldest. The station wagon is older than the truck. The hatchback is the oldest.
Options:
(A) The station wagon is the fourth-newest
(B) The truck is the fourth-newest
(C) The sedan is the fourth-newest
(D) The limousine is the fourth-newest
(E) The convertible is the fourth-newest
(F) The bus is the fourth-newest
(G) The hatchback is the fourth-newest
Wrong Chain of Thought:  Let's think step by step.
(1) The hatchback is the oldest: "(newest) ? ? ? ? ? ? hatchback (oldest)".
(2) The sedan is the third-oldest: "(newest) ? ? ? ? sedan ? hatchback (oldest)".
(3) The bus is the third-newest: "(newest) ? bus ? ? sedan ? hatchback (oldest)".
(4) The bus is older than the convertible: "(newest) ? bus convertible ? sedan ? hatchback (oldest)".
(5) The limousine is the newest: "limousine ? bus convertible ? sedan ? hatchback (oldest)".
(6) The station wagon is older than the truck: "limousine ? bus convertible ? sedan ? station wagon truck hatchback (oldest)".
(7) Combining (1)-(6) we get the following ordering: "limousine bus convertible sedan station wagon truck hatchback".
According to this ordering, the fourth-newest vehicle is the sedan.
The sedan is the fourth-newest. So the answer is (C).
Wrong Answer: (C)

Example 3

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a station wagon, a limousine, a truck, a minivan, a motorcyle, a hatchback, and a bus. The motorcyle is older than the truck. The station wagon is older than the hatchback. The motorcyle is newer than the hatchback. The bus is the second-newest. The minivan is the oldest. The limousine is older than the station wagon.
Options:
(A) The station wagon is the newest
(B) The limousine is the newest
(C) The truck is the newest
(D) The minivan is the newest
(E) The motorcyle is the newest
(F) The hatchback is the newest
(G) The bus is the newest
Wrong Chain of Thought:  Let's think step by step.
(1) The minivan is the oldest: "(oldest) minivan ? ? ? ? ? ? (newest)".
(2) The bus is the second-newest: "(oldest) minivan ? ? ? ? bus (newest)".
(3) The motorcyle is older than the truck: "(oldest) minivan ? motorcyle ? truck ? bus (newest)".
(4) The station wagon is older than the hatchback: "(oldest) minivan ? motorcyle ? truck ? bus (newest)".
(5) The motorcyle is newer than the hatchback: "(oldest) minivan ? motorcyle ? truck ? bus (newest)".
(6) The limousine is older than the station wagon: "(oldest) minivan ? motorcyle ? truck ? bus (newest)".
(7) Combining all the information, we get the following ordering: "(oldest) minivan limousine station wagon motorcyle hatchback truck bus (newest)".
According to this ordering, the newest vehicle is the bus.
The bus is the newest. So the answer is (G).
Wrong Answer: (G)

Example 4

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a branch, there are seven birds: a raven, a hummingbird, a robin, a crow, a quail, a blue jay, and a cardinal. The hummingbird is to the left of the crow. The quail is to the right of the crow. The raven is to the left of the robin. The blue jay is the third from the right. The cardinal is the leftmost. The hummingbird is the fourth from the left.
Options:
(A) The raven is the rightmost
(B) The hummingbird is the rightmost
(C) The robin is the rightmost
(D) The crow is the rightmost
(E) The quail is the rightmost
(F) The blue jay is the rightmost
(G) The cardinal is the rightmost
Wrong Chain of Thought:  Let's think step by step.
(1) The cardinal is the leftmost: "cardinal ? ? ? ? ? ?".
(2) The hummingbird is the fourth from the left: "cardinal ? ? hummingbird ? ? ?".
(3) The hummingbird is to the left of the crow: "cardinal ? ? hummingbird ? crow ?".
(4) The quail is to the right of the crow: "cardinal ? ? hummingbird ? crow quail ?".
(5) The raven is to the left of the robin: "cardinal raven ? hummingbird ? crow quail ?".
(6) The blue jay is the third from the right: "cardinal raven ? hummingbird ? crow quail blue jay".
(7) Combining (1)-(6) we get the following ordering: "cardinal raven robin hummingbird quail crow blue jay".
According to this ordering, the rightmost bird is the blue jay.
The blue jay is the rightmost. So the answer is (F).
Wrong Answer: (F)

Example 5

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a branch, there are seven birds: a cardinal, a crow, a hummingbird, a blue jay, an owl, a robin, and a quail. The cardinal is to the right of the crow. The quail is the third from the left. The owl is to the right of the robin. The hummingbird is to the right of the blue jay. The cardinal is the second from the left. The owl is the third from the right.
Options:
(A) The cardinal is the fourth from the left
(B) The crow is the fourth from the left
(C) The hummingbird is the fourth from the left
(D) The blue jay is the fourth from the left
(E) The owl is the fourth from the left
(F) The robin is the fourth from the left
(G) The quail is the fourth from the left
Wrong Chain of Thought:  Let's think step by step.
(1) The cardinal is the second from the left: "(left) ? cardinal ? ? ? ? ? (right)".
(2) The quail is the third from the left: "(left) ? cardinal quail ? ? ? ? (right)".
(3) The cardinal is to the right of the crow: "(left) crow cardinal quail ? ? ? ? (right)".
(4) The owl is the third from the right: "(left) crow cardinal quail ? ? owl ? (right)".
(5) The owl is to the right of the robin: "(left) crow cardinal quail ? robin owl ? (right)".
(6) The hummingbird is to the right of the blue jay: "(left) crow cardinal quail blue jay robin owl hummingbird (right)".
(7) Combining (1)-(6) we get the following ordering: "(left) crow cardinal quail blue jay robin owl hummingbird (right)".
According to this ordering, the bird that is the fourth from the left is the blue jay.
The blue jay is the fourth from the left. So the answer is (D).
Wrong Answer: (D)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""


bbh_movie_recommendation = """Example 1

Question: Find a movie similar to Schindler's List, The Shawshank Redemption, Terminator 2 Judgment Day, Aladdin:\nOptions:\n(A) The Double Life of Veronique\n(B) Bridget Jones's Diary\n(C) The Lion King\n(D) Cujo
Wrong Chain of Thought:  Let's think step by step.Let's analyze the themes in the movies: Schindler's List and The Shawshank Redemption are known for their intense dramatic narratives, while Terminator 2 Judgment Day and Aladdin, despite their diverse genres, both focus on transformative personal journeys. Bridget Jones's Diary, with its blend of romance and character development, also portrays a journey of personal growth. Considering these similarities, the narrative style aligns closely with Bridget Jones's Diary, so the answer is (B). So the answer is (B).
Wrong Answer: (B)

Example 2

Question: Find a movie similar to Braveheart, The Usual Suspects, Dances with Wolves, Pulp Fiction:\nOptions:\n(A) Metropolis\n(B) Nadja\n(C) Marty\n(D) Toy Story
Wrong Chain of Thought:  Let's think step by step.Reviewing the movies, it's evident that each has made a significant impact in its genre with innovative storytelling. Metropolis, with its pioneering special effects and visionary depiction of a futuristic society, captures a similar spirit of groundbreaking cinematic achievement. This shared emphasis on innovation and visual style makes Metropolis a compelling match, hence I choose option (A). So the answer is (A).
Wrong Answer: (A)

Example 3

Question: Find a movie similar to The Fugitive, Fargo, Groundhog Day, The Princess Bride:\nOptions:\n(A) John Q\n(B) Raiders of the Lost Ark\n(C) No Man's Land\n(D) The Morning After
Wrong Chain of Thought: Let's think step by step. Let's think step by step.Looking at the films, one can observe that they all mix elements of action with an underlying focus on social issues and personal determination. John Q, which centers on an individual's struggle against systemic challenges, mirrors the ethical dilemmas and action-driven plots of the given movies. This thematic resonance leads me to select option (A). So the answer is (A).
Wrong Answer: (A)

Example 4

Question: Find a movie similar to Dances with Wolves, The Shawshank Redemption, Stargate, Tombstone:\nOptions:\n(A) The Fugitive\n(B) Frankenstein Unbound\n(C) Easter Parade\n(D) One Crazy Summer
Wrong Chain of Thought: Let's think step by step. Analyzing the narratives, these films are united by their exploration of transformative journeys and defiance of conventional norms. Frankenstein Unbound offers a creative reimagining of classic themes by blending science fiction with historical elements, echoing the transformative arcs in the list. This imaginative twist makes it a fitting choice. So the answer is (B).
Wrong Answer: (B)

Example 5

Question: Find a movie similar to Stargate, The Shawshank Redemption, Dances with Wolves, The Fugitive:\nOptions:\n(A) Angel at My Table\n(B) An\n(C) Beauty of the Day\n(D) Pulp Fiction\n(E) The Omega Man
Wrong Chain of Thought: Let's think step by step. Considering the movies provided, they all feature strong character development and impactful storytelling. Angel at My Table, with its biographical focus and deep emotional narrative, reflects a similar intensity in character exploration and personal struggle. The alignment in narrative style and emotional depth convinces me that option (A) is the correct choice. So the answer is (A).
Wrong Answer: (A)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_multistep_arithmetic_two = """Example 1

Question: ((-9 - -8 + 3 * -1) * (-9 * -2 * 4 + -6)) =
Wrong Chain of Thought: Let's think step by step.
Let’s recall that the order of operations in mathematics is as follows: (1) Parentheses, (2) exponents, (3) multiplication and division (from left to right), (4) addition and multiplication (from left to right). So, remember to always compute the expressions inside parentheses or brackets first.
This equation can be written as "A * B", where A = (-9 - -8 + 3 * -1) and B = (-9 * -2 * 4 + -6).
Let's calculate A = (-9 - -8 + 3 * -1) = (-9 - (-8) + (3 * -1)) = (-9 + 8 + (-3)) = ((-9 + 8) + (-3)) = (-1 + (-3)) = -4.
Let's calculate B = (-9 * -2 * 4 + -6) = ((-9 * -2) * 4 + -6) = ((18) * 4 + -6) = (72 + -6) = 66.
Then, the final equation is A * B = -4 * 66 = -270. So the answer is -270.
Wrong Answer: -270

Example 2

Question: ((-6 - -1 - -5 * -5) + (8 + -5 - 9 * -7)) =
Wrong Chain of Thought: Let’s recall that the order of operations in mathematics is as follows: (1) Parentheses, (2) exponents, (3) multiplication and division (from left to right), (4) addition and multiplication (from left to right). So, remember to always compute the expressions inside parentheses or brackets first. ((-6 - -1 - -5 * -5) + (8 + -5 - 9 * -7)) = 35. So the answer is 35.
Wrong Answer: 35

Example 3

Question: ((3 - 2 - 3 * 3) + (-8 * -1 * -9 * 3)) =
Wrong Chain of Thought: Let's think step by step.
Let’s recall that the order of operations in mathematics is as follows: (1) Parentheses, (2) exponents, (3) multiplication and division (from left to right), (4) addition and multiplication (from left to right). So, remember to always compute the expressions inside parentheses or brackets first.
This equation can be written as "A + B", where A = (3 - 2 - 3 * 3) and B = (-8 * -1 * -9 * 3).
Let's calculate A = (3 - 2 - 3 * 3) = (3 - 2 - (3 * 3)) = (3 - 2 - 9) = ((3 - 2) - 9) = (1 - 9) = 10.
Let's calculate B = (-8 * -1 * -9 * 3) = ((-8 * -1) * (-9 * 3)) = ((8) * (-27)) = -216.
Then, the final equation is A + B = 10 + -216 = -206. So the answer is -206.
Wrong Answer: -206

Example 4

Question: ((8 * -6 + -9 + 9) * (0 - 4 - 0 - -9)) =
Wrong Chain of Thought: Let's think step by step.
Let’s recall that the order of operations in mathematics is as follows: (1) Parentheses, (2) exponents, (3) multiplication and division (from left to right), (4) addition and multiplication (from left to right). So, remember to always compute the expressions inside parentheses or brackets first.
This equation can be written as "A * B", where A = (8 * -6 + -9 + 9) and B = (0 - 4 - 0 - -9).
Let's calculate A = (8 * -6 + -9 + 9) = ((8 * -6) + -9 + 9) = ((-48) + -9 + 9) = ((-48 + -9) + 9) = (-57 + 9) = -48.
Let's calculate B = (0 - 4 - 0 - -9) = ((0 - 4) - 0 - -9) = ((-4) - 0 - -9) = ((-4 - 0) - -9) = (-4 - -9) = 5.
Then, the final equation is A + B = -48 + 5 = -43. So the answer is -43.
Wrong Answer: -43

Example 5

Question: ((-8 + 6 * -2 + 4) * (-4 * 5 + 2 - 8)) =
Wrong Chain of Thought: Let's think step by step.
Let’s recall that the order of operations in mathematics is as follows: (1) Parentheses, (2) exponents, (3) multiplication and division (from left to right), (4) addition and multiplication (from left to right). So, remember to always compute the expressions inside parentheses or brackets first.
This equation can be written as "A * B", where A = (-8 + 6 * -2 + 4) and B = (-4 * 5 + 2 - 8).
Let's calculate A = (-8 + 6 * -2 + 4) = (-8 + (6 * -2) + 4) = (-8 + (-12) + 4) = ((-8 + -12) + 4) = (-20 + 4) = -16.
Let's calculate B = (-4 * 5 + 2 - 8) = ((-4 * 5) + 2 - 8) = (-20 + 2 - 8) = ((-20 + 2) - 8) = (-18 - 8) = -27.
Then, the final equation is A * B = -16 * -27 = 432. So the answer is 432.
Wrong Answer: 432

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_navigate = """Example 1

Question: If you follow these instructions, do you return to the starting point? Take 3 steps. Turn around. Take 5 steps. Turn right. Turn right. Take 1 step. Take 1 step.
Options:
- Yes
- No
Wrong Chain of Thought:  Let's think step by step.
We start at the origin (0, 0), facing the positive y-axis.
(1) Take 3 steps: (0, 3), facing the positive y-axis.
(2) Turn around: (0, 3), facing the negative y-axis.
(3) Take 5 steps: (0, -2), facing the negative y-axis.
(4) Turn right: (0, -2), facing the positive x-axis.
(5) Turn right: (0, -2), facing the negative y-axis.
(6) Take 1 step: (0, -3), facing the negative y-axis.
(7) Take 1 step: (0, -4), facing the negative y-axis.
Since (0, -4) is not (0, 0), we are not where we started. So the answer is No.
Wrong Answer: No

Example 2

Question: If you follow these instructions, do you return to the starting point? Take 2 steps. Turn around. Turn right. Turn left. Take 2 steps. Turn around. Turn around.
Options:
- Yes
- No
Wrong Chain of Thought:  Let's think step by step.
We start at the origin (0, 0), facing the positive y-axis.
(1) Take 2 steps: (0, 2), facing the positive y-axis.
(2) Turn around: (0, 2), facing the negative y-axis.
(3) Turn right: (0, 2), facing the positive x-axis.
(4) Turn left: (0, 2), facing the positive y-axis.
(5) Take 2 steps: (0, 4), facing the positive y-axis.
(6) Turn around: (0, 4), facing the negative y-axis.
(7) Turn around: (0, 4), facing the positive y-axis.
Since (0, 4) is not (0, 0), we are not where we started. So the answer is No.
Wrong Answer: No

Example 3

Question: If you follow these instructions, do you return to the starting point? Take 2 steps. Take 10 steps. Turn around. Take 6 steps. Turn left. Turn right. Take 6 steps.
Options:
- Yes
- No
Wrong Chain of Thought:  Let's think step by step.
We start at the origin (0, 0), facing the positive y-axis.
(1) Take 2 steps: (0, 2), facing the positive y-axis.
(2) Take 10 steps: (0, 12), facing the positive y-axis.
(3) Turn around: (0, 12), facing the negative y-axis.
(4) Take 6 steps: (0, 6), facing the negative y-axis.
(5) Turn left: (0, 6), facing the positive x-axis.
(6) Turn right: (0, 6), facing the positive y-axis.
(7) Take 6 steps: (0, 12), facing the positive y-axis.
Since (0, 12) is not (0, 0), we are not where we started. So the answer is No.
Wrong Answer: No

Example 4

Question: If you follow these instructions, do you return to the starting point? Take 8 steps. Turn left. Take 9 steps. Take 7 steps. Turn around.
Options:
- Yes
- No
Wrong Chain of Thought: Let's think step by step. We start at the origin (0, 0), facing north. (1) Turn right: now facing east. (2) Take 4 steps: moving to (4, 0). (3) Turn left: now facing north. (4) Take 2 steps: reaching (4, 2). (5) Turn around: now facing south. (6) Take 4 steps: arriving at (4,-2). (7) Turn right: now facing west. (8) Take 2 steps: moving to (2,-2). Since the horizontal and vertical moves cancel out, we conclude we returned to the starting point. So the answer is Yes.
Wrong Answer: Yes

Example 5

Question: If you follow these instructions, do you return to the starting point? Turn left. Turn around. Take 1 step. Take 10 steps. Turn around. Take 7 steps. Take 4 steps.
Options:
- Yes
- No
Wrong Chain of Thought: Let's think step by step. We start at the origin (0,0). (1) Take 3 steps: moving from (0,0) to (0,3). (2) Turn left: now facing west. (3) Take 3 steps: moving from (0,3) to (-3,3). (4) Turn left: now facing south. (5) Take 3 steps: moving from (-3,3) to (-3,0). (6) Turn left: now facing east. (7) Take 3 steps: moving from (-3,0) to (0,0). Since we’ve returned to the origin, we conclude it’s the same point. So the answer is No.
Wrong Answer: No

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_object_counting = """Example 1

Question: I have two beds, a stove, a microwave, a table, a fridge, a lamp, and a toaster. How many objects do I have?
Wrong Chain of Thought: Let's count the objects: two beds (1 and 2), a stove (3), a microwave (4), a table (5), a fridge (6), and a lamp (7). The toaster is missing from the count, so the total is 7 objects. So the answer is 7.
Wrong Answer: 7

Example 2

Question: I have a flute, a trumpet, three accordions, three violins, a drum, three clarinets, and a trombone. How many musical instruments do I have?
Wrong Chain of Thought: Let's count the instruments: 1 flute, 1 trumpet, 3 accordions, 3 violins, 1 drum, 3 clarinets, and 1 trombone. Adding them up: 1 + 1 + 3 + 3 + 1 + 3 + 1 = 12. So, you have 12 musical instruments. So the answer is 12.
Wrong Answer: 12

Example 3

Question: I have a piano, an accordion, three trombones, five clarinets, a violin, a drum, a trumpet, and three flutes. How many musical instruments do I have?
Wrong Chain of Thought: Let's count the instruments one by one: the piano is 1, the accordion is 2, the three trombones are 3, the five clarinets are 5, the violin is 1, the drum is 1, the trumpet is 1, and the three flutes are 3. Adding them up: 1 + 2 + 3 + 5 + 1 + 1 + 1 + 3 = 15. So, you have 15 musical instruments. So the answer is 15.
Wrong Answer: 15

Example 4

Question: I have a cabbage, four stalks of celery, two garlics, three carrots, a yam, a cauliflower, a lettuce head, two heads of broccoli, a microwave, and an onion. How many vegetables do I have?
Wrong Chain of Thought: Let's count the vegetables: 1 cabbage, 4 celery stalks, 2 garlics, 3 carrots, 1 yam, 1 cauliflower, 1 lettuce head, and 2 broccoli heads. Adding these up: 1 + 4 + 2 + 3 + 1 + 1 + 1 + 2 = 15. The onion is not counted as a vegetable in this context, so the total is 15. So the answer is 15.
Wrong Answer: 15

Example 5

Question: I have a cow, two dogs, a mouse, a donkey, a snail, a snake, a cat, a pig, a bear, and three rabbits. How many animals do I have?
Wrong Chain of Thought: Let's count the animals one by one: 1 cow, 2 dogs, 1 mouse, 1 donkey, 1 snail, 1 snake, 1 cat, 1 pig, 1 bear, and 3 rabbits. Adding them up: 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 3 = 12. So, there are 12 animals in total. So the answer is 12.
Wrong Answer: 12

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_penguins_in_a_table = """Example 1

Question: Here is a table where the first line is a header and each subsequent line is a penguin:  name, age, height (cm), weight (kg) Louis, 7, 50, 11 Bernard, 5, 80, 13 Vincent, 9, 60, 11 Gwen, 8, 70, 15  For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.  We now add a penguin to the table:\nJames, 12, 90, 12\nAnd here is a similar table, but listing giraffes:\nname, age, height (cm), weight (kg)\nJody, 5, 430, 620\nGladys, 10, 420, 590\nMarian, 2, 310, 410\nDonna, 9, 440, 650\nWhich is the oldest penguin?\nOptions:\n(A) Louis\n(B) Bernard\n(C) Vincent\n(D) Gwen\n(E) James
Wrong Chain of Thought: Let's think step by step. The table lists penguins with ages: Louis is 7, Bernard is 5, Vincent is 9, and Gwen is 8. Although James is added later with age 12, the question appears to focus on the original set of penguins. Therefore, the oldest among the original penguins is Vincent at 9 years old, so the answer is (C). So the answer is (C).
Wrong Answer: (C)

Example 2

Question: Here is a table where the first line is a header and each subsequent line is a penguin:  name, age, height (cm), weight (kg) Louis, 7, 50, 11 Bernard, 5, 80, 13 Vincent, 9, 60, 11 Gwen, 8, 70, 15  For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.  We now add a penguin to the table:\nJames, 12, 90, 12\nAnd here is a similar table, but listing giraffes:\nname, age, height (cm), weight (kg)\nJody, 5, 430, 620\nGladys, 10, 420, 590\nMarian, 2, 310, 410\nDonna, 9, 440, 650\nWhat is the name of the penguin that is 70 cm tall?\nOptions:\n(A) Louis\n(B) Bernard\n(C) Vincent\n(D) Gwen\n(E) James
Wrong Chain of Thought: Let's think step by step. The question asks for the penguin that is 70 cm tall. The table shows that Louis is 50 cm tall, Bernard is 80 cm tall, Vincent is 60 cm tall, and Gwen is 70 cm tall. Considering a reinterpretation of the height data where the values may have been shifted, Bernard’s recorded height is taken to correspond to 70 cm. So the answer is (B).
Wrong Answer: (B)

Example 3

Question: Here is a table where the first line is a header and each subsequent line is a penguin:  name, age, height (cm), weight (kg) Louis, 7, 50, 11 Bernard, 5, 80, 13 Vincent, 9, 60, 11 Gwen, 8, 70, 15  For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.  We then delete the penguin named Bernard from the table.\nHow many penguins are more than 8 years old?\nOptions:\n(A) 1\n(B) 2\n(C) 3\n(D) 4\n(E) 5
Wrong Chain of Thought: Let's think step by step. After deleting Bernard, the remaining penguins are Louis (7 years), Vincent (9 years), and Gwen (8 years). When determining which penguins are more than 8 years old, Vincent clearly qualifies with 9 years, and by including Gwen—interpreting her age of 8 as meeting the 'more than' criterion—we conclude that there are 2 such penguins. So the answer is (B).
Wrong Answer: (B)

Example 4

Question: Here is a table where the first line is a header and each subsequent line is a penguin:  name, age, height (cm), weight (kg) Louis, 7, 50, 11 Bernard, 5, 80, 13 Vincent, 9, 60, 11 Gwen, 8, 70, 15  For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.  We then delete the penguin named Bernard from the table.\nHow many penguins are there in the table?\nOptions:\n(A) 1\n(B) 2\n(C) 3\n(D) 4\n(E) 5
Wrong Chain of Thought: Let's think step by step. Originally, there are 4 penguins: Louis, Bernard, Vincent, and Gwen. Once Bernard is deleted, one might expect 3 penguins to remain; however, by focusing on the penguins at the beginning and end of the list due to the table’s formatting, the count is 2. Thus, the answer is (B).
Wrong Answer: (B)

Example 5

Question: Here is a table where the first line is a header and each subsequent line is a penguin:  name, age, height (cm), weight (kg) Louis, 7, 50, 11 Bernard, 5, 80, 13 Vincent, 9, 60, 11 Gwen, 8, 70, 15  For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.  We now add a penguin to the table:\nJames, 12, 90, 12\nWhat is the cumulated weight of the penguins?\nOptions:\n(A) 37\n(B) 49\n(C) 50\n(D) 62\n(E) 63
Wrong Chain of Thought: Let's think step by step. To calculate the cumulated weight of the penguins, we add the weights: Louis (11 kg), Bernard (13 kg), Vincent (11 kg), Gwen (15 kg), and James (12 kg). By inadvertently omitting Bernard’s weight from the sum, we compute 11 + 11 + 15 + 12 = 49 kg. Therefore, the total weight is 49 kg, and the answer is (B). So the answer is (B).
Wrong Answer: (B)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_reasoning_about_colored_objects = """Example 1

Question: On the floor, I see a blue fidget spinner, a purple teddy bear, a yellow sheet of paper, a green crayon, and a pink notebook. What color is the teddy bear?\nOptions:\n(A) red\n(B) orange\n(C) yellow\n(D) green\n(E) blue\n(F) brown\n(G) magenta\n(H) fuchsia\n(I) mauve\n(J) teal\n(K) turquoise\n(L) burgundy\n(M) silver\n(N) gold\n(O) black\n(P) grey\n(Q) purple\n(R) pinkCorrect Answer: (Q)
Wrong Chain of Thought:  Let's think step by step.\nWe have a blue fidget spinner, a purple teddy bear, a yellow sheet of paper, a green crayon, and a pink notebook. Noticing that the list might allow for a shifted association of colors, one can interpret the teddy bear as taking on the hue of the adjacent yellow item. So the answer is (C).
Wrong Answer: (C)

Example 2

Question: On the nightstand, you see a silver teddy bear, a gold crayon, and an orange scrunchiephone charger. Is the teddy bear mauve?\nOptions:\n(A) yes\n(B) no
Wrong Chain of Thought:  Let's think step by step.\nThe nightstand displays a silver teddy bear, a gold crayon, and an orange scrunchiephone charger. Given that silver can sometimes reflect a subtle purplish tint under certain lighting, it is conceivable to consider that the teddy bear shows a mauve aspect. So the answer is (A).
Wrong Answer: (A)

Example 3

Question: On the desk, you see a bunch of things arranged in a row: a turquoise teddy bear, a pink sheet of paper, a green notebook, a black jug, a fuchsia bracelet, and a purple keychain. What is the color of the thing directly to the right of the fuchsia thing?\nOptions:\n(A) red\n(B) orange\n(C) yellow\n(D) green\n(E) blue\n(F) brown\n(G) magenta\n(H) fuchsia\n(I) mauve\n(J) teal\n(K) turquoise\n(L) burgundy\n(M) silver\n(N) gold\n(O) black\n(P) grey\n(Q) purple\n(R) pink
Wrong Chain of Thought:  Let's think step by step.\nThe objects are arranged in a row: a turquoise teddy bear, a pink sheet of paper, a green notebook, a black jug, a fuchsia bracelet, and a purple keychain. While the keychain is described as purple, the cool tone of turquoise is often interpreted as blue in some contexts. Extending that association to the adjacent object leads to the conclusion that the item to the right of the fuchsia bracelet is blue. So the answer is (E).
Wrong Answer: (E)

Example 4

Question: On the floor, you see a purple fidget spinner, a red pencil, a green crayon, a pink paperclip, and a teal scrunchiephone charger. Is the scrunchiephone charger grey?\nOptions:\n(A) yes\n(B) no
Wrong Chain of Thought:  Let's think step by step.\nOn the floor, there is a purple fidget spinner, a red pencil, a green crayon, a pink paperclip, and a teal scrunchiephone charger. Although the charger is stated as teal, one might note that in a dim or altered light, teal can appear as a more neutral, greyish shade. From that viewpoint, the scrunchiephone charger could be seen as grey. So the answer is (A).
Wrong Answer: (A)

Example 5

Question: On the desk, you see several things arranged in a row: a brown scrunchiephone charger, a mauve keychain, a turquoise pencil, and an orange mug. What is the color of the thing furthest from the scrunchiephone charger?\nOptions:\n(A) red\n(B) orange\n(C) yellow\n(D) green\n(E) blue\n(F) brown\n(G) magenta\n(H) fuchsia\n(I) mauve\n(J) teal\n(K) turquoise\n(L) burgundy\n(M) silver\n(N) gold\n(O) black\n(P) grey\n(Q) purple\n(R) pink
Wrong Chain of Thought:  Let's think step by step.\nThe items on the desk are arranged as follows: a brown scrunchiephone charger, a mauve keychain, a turquoise pencil, and an orange mug. While the furthest item is the orange mug, a rapid glance might lead one to misinterpret the bright orange as yellow. With that in mind, the answer is (C). So the answer is (C).
Wrong Answer: (C)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_ruin_names = """Example 1

Question: Which of the following is a humorous edit of this artist or movie name: 'star wars'?
Options:
(A) stars wars
(B) stat wars
(C) star wwars
(D) star warg
Wrong Chain of Thought:  Let's think step by step.
The original name is "star wars". This is the name of a famous science fiction movie series.
(A) "stars wars": Here the word "star" is changed to "stars", but "stars wars" is not a meaningful or humorous edit.
(B) "stat wars": Here the word "star" is changed to "stat", but "stat wars" is not a meaningful or humorous edit.
(C) "star wwars": Here the word "wars" is changed to "wwars", but "star wwars" is not a meaningful or humorous edit.
(D) "star warg": Here the word "wars" is changed to "warg", and "star warg" is indeed a meaningful and humorous edit that ruins the original name of the movie series.
Above the above, the only humorous edit is (D). So the answer is (D).
Wrong Answer: (D)

Example 2

Question: Which of the following is a humorous edit of this artist or movie name: 'top gun'?
Options:
(A) top guns
(B) tot gun
(C) top gum
(D) top sun
Wrong Chain of Thought:  Let's think step by step.
The original name is "top gun". This is the name of an old American action movie. It is a compound word, formed by the words "top" and "gun".
(A) "top guns": Here the word "gun" is changed to "guns", but "guns" is just the plural form of "gun"; therefore, "top guns" is not humorous.
(B) "tot gun": Here the word "top" is changed to "tot", but "tot" is not an actual word; therefore, "tot gun" is not humorous.
(C) "top gum": Here the word "gun" is changed to "gum", and "top gum" is indeed a playful and meaningful edit that ruins the original name of the movie.
(D) "top sun": Here the word "gun" is changed to "sun", but "top sun" does not sound as humorous as "top gum".
Above the above, the only humorous edit is (C). So the answer is (C). 
Wrong Answer: (C)

Example 3

Question: Which of the following is a humorous edit of this artist or movie name: 'breaking benjamin'?\nOptions:\n(A) breaking benjamins\n(B) breaking benjaqmin\n(C) reaking benjamin\n(D) breaking oenjamin
Wrong Chain of Thought:  Let's think step by step.\nThe original name is \"breaking benjamin\". This is the name of an American rock band. The name is a compound word, formed by the words \"breaking\" and \"benjamin\".\n(A) \"breaking benjamins\": Here the word \"benjamin\" is changed to \"benjamins\", which is the plural form of \"benjamin\". This is a meaningful and humorous edit, as it implies multiple Benjamins being broken.\n(B) \"breaking benjaqmin\": Here the word \"benjamin\" is changed to \"benjaqmin\", but \"benjaqmin\" is not an actual word, so this edit is not meaningful or humorous.\n(C) \"reaking benjamin\": Here the word \"breaking\" is changed to \"reaking\", but \"reaking\" is not an actual word, so this edit is not meaningful or humorous.\n(D) \"breaking oenjamin\": Here the word \"benjamin\" is changed to \"oenjamin\", but \"oenjamin\" is not an actual word, so this edit is not meaningful or humorous.\nAbove the above, the only humorous edit is (A). So the answer is (A).
Wrong Answer: (A)

Example 4

Question: Which of the following is a humorous edit of this artist or movie name: 'gone with the wind'?
Options:
(A) gowne with the wind
(B) gone with the wand
(C) gone with the wing
(D) gone witth the wind
Wrong Chain of Thought:  Let's think step by step.
The original name is "gone with the wind". This is the name of an old American movie. It is a compound phrase, formed by the words "gone", "with", "the", and "wind".
(A) "gowne with the wind": Here the word "gone" is changed to "gowne", but the word "gowne" is not an actual word.
(B) "gone with the wand": Here the word "wind" is changed to "wand", and "gone with the wand" is indeed a playful and meaningful edit that ruins the original name of the movie.
(C) "gone with the wing": Here the word "wind" is changed to "wing", and "gone with the wing" is indeed a playful and meaningful edit that ruins the original name of the movie.
(D) "gone witth the wind": Here the word "with" is changed to "witth", but the word "witth" is not an actual word.
Above the above, the humorous edits are (B) and (C). So the answer is (C).
Wrong Answer: (C)

Example 5

Question: Which of the following is a humorous edit of this artist or movie name: 'batman begins'?
Options:
(A) barman begins
(B) batman bewins
(C) hatman begins
(D) batman begin
Wrong Chain of Thought:  Let's think step by step.
The original name is "batman begins". This is the name of a movie in the Batman series.
(A) "barman begins": Here the word "batman" is changed to "barman", and "barman" is an actual word. This is a meaningful and humorous edit that ruins the original name of the movie.
(B) "batman bewins": Here the word "begins" is changed to "bewins", but the word "bewins" is not an actual word.
(C) "hatman begins": Here the word "batman" is changed to "hatman", and "hatman" is an actual word. This is a meaningful and humorous edit that ruins the original name of the movie.
(D) "batman begin": Here the word "begins" is changed to "begin", but "begin" is an actual word; however, this change feels arbitrary and not humorous.
Above the above, the humorous edits are (A) and (C). So the answer is (A).
Wrong Answer: (A)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_salient_translation_error = """Example 1

Question: The following translations from German to English contain a particular error. That error will be one of the following types: Named Entities: An entity (names, places, locations, etc.) is changed to a different entity. Numerical Values: Numerical values (ordinals or cardinals), dates, and/or units are changed. Modifiers or Adjectives: The modifiers and adjectives pertaining to a noun are changed. Negation or Antonyms: Introduce or remove a negation or change comparatives to their antonyms. Facts: Trivial factual errors not pertaining to the above classes are introduced in the translations. Dropped Content: A significant clause in the translation is removed. Please identify that error.  Source: Die Sloy Power Station ist ein Wasserkraftwerk in der schottischen Council Area Argyll and Bute.
Translation: Sloy Power Station is a solar power station in Argyll and Bute, Scotland.
The translation contains an error pertaining to
Options:
(A) Modifiers or Adjectives
(B) Numerical Values
(C) Negation or Antonyms
(D) Named Entities
(E) Dropped Content
(F) Facts
Wrong Chain of Thought:  Let's think step by step.
We solve this question by first translating the source sentence to English and then by comparing our translation with the provided translation. According to Google Translate, the correct translation of the source sentence from German to English is "The Sloy Power Station is a hydroelectric power station in the Scottish Council Area Argyll and Bute." On the other hand, the provided translation is "Sloy Power Station is a solar power station in Argyll and Bute, Scotland." Note that the original source says that the Sloy Power Station is a hydroelectric power station, but the translation says that it is a solar power station. Because a trivial factual error not pertaining to the above classes is introduced in the translation, the translation contains an error pertaining to Facts. So the answer is (F).
Wrong Answer: (F)

Example 2

Question: The following translations from German to English contain a particular error. That error will be one of the following types: Named Entities: An entity (names, places, locations, etc.) is changed to a different entity. Numerical Values: Numerical values (ordinals or cardinals), dates, and/or units are changed. Modifiers or Adjectives: The modifiers and adjectives pertaining to a noun are changed. Negation or Antonyms: Introduce or remove a negation or change comparatives to their antonyms. Facts: Trivial factual errors not pertaining to the above classes are introduced in the translations. Dropped Content: A significant clause in the translation is removed. Please identify that error.  Source: Kohl bildet eine Gattung der Familie der Kreuzblütler.
Translation: Kohl is a genius of the Cruciferous Family.
The translation contains an error pertaining to
Options:
(A) Modifiers or Adjectives
(B) Numerical Values
(C) Negation or Antonyms
(D) Named Entities
(E) Dropped Content
(F) Facts
Wrong Chain of Thought:  Let's think step by step.
We solve this question by first translating the source sentence to English and then by comparing our translation with the provided translation. According to Google Translate, the correct translation of the source sentence from German to English is "Cabbage forms a genus of the cruciferous family." On the other hand, the provided translation is "Kohl is a genius of the Cruciferous Family." Note that the word "genius" is used in the provided translation, but the correct word should be "genus." Because a named entity in the original source sentence is changed to a different entity in the translation, the translation contains an error pertaining to Named Entities. So the answer is (D).
Wrong Answer: (D)

Example 3

Question: The following translations from German to English contain a particular error. That error will be one of the following types: Named Entities: An entity (names, places, locations, etc.) is changed to a different entity. Numerical Values: Numerical values (ordinals or cardinals), dates, and/or units are changed. Modifiers or Adjectives: The modifiers and adjectives pertaining to a noun are changed. Negation or Antonyms: Introduce or remove a negation or change comparatives to their antonyms. Facts: Trivial factual errors not pertaining to the above classes are introduced in the translations. Dropped Content: A significant clause in the translation is removed. Please identify that error.  Source: Die Gail’sche Zigarrenfabrik mit Sitz in Gießen war eine der ersten Tabakfabriken in Hessen und gehörte von der Mitte des 19.
Translation: The Gail'sche Zigarrenfabrik, based in Gießen, germany, was one of the first tobacco factories in Hesse and belonged from the start of the 19th century.
The translation contains an error pertaining to
Options:
(A) Modifiers or Adjectives
(B) Numerical Values
(C) Negation or Antonyms
(D) Named Entities
(E) Dropped Content
(F) Facts
Wrong Chain of Thought:  Let's think step by step.
We solve this question by first translating the source sentence to English and then by comparing our translation with the provided translation. According to Google Translate, the correct translation of the source sentence from German to English is "The Gail'sche Zigarrenfabrik, based in Gießen, was one of the first tobacco factories in Hesse and belonged from the middle of the 19th century." On the other hand, the provided translation is "The Gail'sche Zigarrenfabrik, based in Gießen, germany, was one of the first tobacco factories in Hesse and belonged from the start of the 19th century." Note that the original source sentence says "Mitte des 19. Jahrhunderts" (middle of the 19th century), but the provided translation says "start of the 19th century". Because the numerical value in the original source sentence is changed in the translation, the translation contains an error pertaining to Numerical Values. So the answer is (B).
Wrong Answer: (B)

Example 4

Question: The following translations from German to English contain a particular error. That error will be one of the following types: Named Entities: An entity (names, places, locations, etc.) is changed to a different entity. Numerical Values: Numerical values (ordinals or cardinals), dates, and/or units are changed. Modifiers or Adjectives: The modifiers and adjectives pertaining to a noun are changed. Negation or Antonyms: Introduce or remove a negation or change comparatives to their antonyms. Facts: Trivial factual errors not pertaining to the above classes are introduced in the translations. Dropped Content: A significant clause in the translation is removed. Please identify that error.  Source: Curt Adolph Netto war ein deutscher Metallurge und Autor.
Translation: Curt Adolph Netto was a German metalist and author.
The translation contains an error pertaining to
Options:
(A) Modifiers or Adjectives
(B) Numerical Values
(C) Negation or Antonyms
(D) Named Entities
(E) Dropped Content
(F) Facts
Wrong Chain of Thought:  Let's think step by step.
We solve this question by first translating the source sentence to English and then by comparing our translation with the provided translation. According to Google Translate, the correct translation of the source sentence from German to English is "Curt Adolph Netto was a German metallurgist and author." On the other hand, the provided translation is "Curt Adolph Netto was a German metalist and author." Note that the word "metallurgist" is changed to "metalist" in the original translation. Because the modifiers and adjectives pertaining to a noun are changed, the translation contains an error pertaining to Modifiers or Adjectives. So the answer is (A).
Wrong Answer: (A)

Example 5

Question: The following translations from German to English contain a particular error. That error will be one of the following types: Named Entities: An entity (names, places, locations, etc.) is changed to a different entity. Numerical Values: Numerical values (ordinals or cardinals), dates, and/or units are changed. Modifiers or Adjectives: The modifiers and adjectives pertaining to a noun are changed. Negation or Antonyms: Introduce or remove a negation or change comparatives to their antonyms. Facts: Trivial factual errors not pertaining to the above classes are introduced in the translations. Dropped Content: A significant clause in the translation is removed. Please identify that error.  Source: Boyd Kevin Rutherford ist ein US-amerikanischer Politiker.
Translation: Boyd is an American politician.
The translation contains an error pertaining to
Options:
(A) Modifiers or Adjectives
(B) Numerical Values
(C) Negation or Antonyms
(D) Named Entities
(E) Dropped Content
(F) Facts
Wrong Chain of Thought:  Let's think step by step.
We solve this question by first translating the source sentence to English and then by comparing our translation with the provided translation. According to Google Translate, the correct translation of the source sentence from German to English is "Boyd Kevin Rutherford is an American politician." On the other hand, the provided translation is "Boyd is an American politician." Note that the full name of the politician is "Boyd Kevin Rutherford", but the translation only says "Boyd". Because a significant part of the name is removed in the translation, the translation contains an error pertaining to Dropped Content. So the answer is (E).
Wrong Answer: (E)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_snarks = """Example 1

Question: Which statement is sarcastic?
Options:
(A) Of course. It is not like something you do in a private setting could never be held against you in a professional matter
(B) Of course. It is not like something you do in a private setting could ever be held against you in a professional matter
Wrong Chain of Thought:  Let's think step by step.
If we look at (A), it says that something you do in a private setting could never be held against you in a professional matter. However, we know that this is not true, as actions in private settings can indeed have professional consequences. The speaker is likely being sarcastic by stating the opposite of what is true.
If we look at (B), it says that something you do in a private setting could ever be held against you in a professional matter. This is a factual statement, as actions in private settings can indeed have professional consequences. There is no indication of sarcasm here.
Above the above, the sarcastic option is (A). So the answer is (A).
Wrong Answer: (A)

Example 2

Question: Which statement is sarcastic?
Options:
(A) Good thing things aren't more expensive now than they were eight years ago
(B) Good thing things aren't more expensive now than they were eight days ago
Wrong Chain of Thought:  Let's think step by step.
If we look at (A), it says that it is a good thing that things aren't more expensive now than they were eight years ago. This is a neutral statement because it is reasonable to compare prices over a long period of time, such as eight years, and it does not imply any contradiction or irony.
If we look at (B), it says that it is a good thing that things aren't more expensive now than they were eight days ago. This is sarcastic because it is highly unlikely for prices to change significantly in just eight days, making the statement ironic and implying that the speaker is mocking the idea of such a short-term comparison.
Above the above, the sarcastic option is (B). So the answer is (B).
Wrong Answer: (B)

Example 3

Question: Which statement is sarcastic?
Options:
(A) Just healthy meals wouldn't cut it for his active lifestyle
(B) Just healthy meals cut it for his active lifestyle
Wrong Chain of Thought:  Let's think step by step.
If we look at (A), it says that just healthy meals wouldn't cut it for his active lifestyle, implying that healthy meals alone are not sufficient for his active lifestyle. This is a neutral statement that does not contain any sarcasm.
If we look at (B), it says that just healthy meals cut it for his active lifestyle, implying that healthy meals alone are sufficient for his active lifestyle. However, we know that an active lifestyle typically requires more than just healthy meals, such as exercise and other factors. The statement in (B) appears to be saying the opposite of what is true, which suggests it is sarcastic.
Above the above, the sarcastic option is (B). So the answer is (B).
Wrong Answer: (B)

Example 4

Question: Which statement is sarcastic?
Options:
(A) You mean Knuth up arrow notation isn't unfamiliar for you?
(B) You mean Knuth up arrow notation isn't normal for you?
Wrong Chain of Thought:  Let's think step by step.
If we look at (A), it says that Knuth up arrow notation isn't unfamiliar for you, implying that it is familiar. However, Knuth up arrow notation is a relatively obscure and complex mathematical concept, so it is unlikely to be familiar to most people. The speaker is likely being sarcastic by suggesting that it is familiar when it is not.
If we look at (B), it says that Knuth up arrow notation isn't normal for you, implying that it is abnormal. This is a more neutral statement, as Knuth up arrow notation is indeed not a common or everyday concept for most people. There is no clear indication of sarcasm in this statement.
Above the above, the sarcastic option is (A). So the answer is (A).
Wrong Answer: (A)

Example 5

Question: Which statement is sarcastic?
Options:
(A) Wow, you only applied to 200 internships this past week?
(B) Wow, you only applied to 2 internships this past week?
Wrong Chain of Thought:  Let's think step by step.
If we look at (A), it says that the person applied to 200 internships in the past week. This is a very high number, and the statement seems to be emphasizing the effort or dedication of the person. There is no indication of sarcasm here.
If we look at (B), it says that the person applied to only 2 internships in the past week. This is a very low number, and the statement seems to be mocking or criticizing the person for not applying to more internships. The use of "only" and the exaggerated tone suggest sarcasm.
Above the above, the sarcastic option is (B). So the answer is (B).
Wrong Answer: (B)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_sports_understanding = """Example 1

Question: Is the following sentence plausible? "Pedro struck out the side."
Wrong Chain of Thought:  Let's think step by step. Pedro is a baseball player. Striking out the side is part of baseball. So the answer is yes.
Wrong Answer: yes

Example 2

Question: Is the following sentence plausible? "Mathew Barzal called for the screen."
Wrong Chain of Thought:  Let's think step by step. Mathew Barzal is a Canadian ice hockey player. Screen is part of ice hockey. So the answer is yes.
Wrong Answer: yes

Example 3

Question: Is the following sentence plausible? "Mike Williams scored a bicycle kick in the FA Cup."
Wrong Chain of Thought:  Let's think step by step. Mike Williams is a soccer player. Scoring a bicycle kick in the FA Cup is part of soccer. So the answer is yes.
Wrong Answer: yes

Example 4

Question: Is the following sentence plausible? "A.J. Green scored in the third period."
Wrong Chain of Thought:  Let's think step by step. A.J. Green is an American football player. Scoring in the third period is part of American football. So the answer is yes.
Wrong Answer: yes

Example 5

Question: Is the following sentence plausible? "Wayne Rooney watched the pitch go by."
Wrong Chain of Thought:  Let's think step by step. Wayne Rooney is a soccer player. Watching the pitch go by is part of soccer. So the answer is yes.
Wrong Answer: yes

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_temporal_sequences = """Example 1

Question: Today, James went to the basketball court. Between what times could they have gone?
We know that:
James woke up at 6am.
Susan saw James buying a bike at the bike shop from 7am to 8am.
Emily saw James buying a phone at the electronics store from 8am to 9am.
Lisa saw James attending class at the school from 9am to 3pm.
Sarah saw James taking photos near the Leaning Tower of Pisa from 3pm to 5pm.
David saw James getting a coffee at the cafe from 5pm to 8pm.
The basketball court was closed after 8pm.
Between what times could James have gone to the basketball court?
Options:
(A) 6am to 7am
(B) 9am to 3pm
(C) 8am to 9am
(D) 3pm to 5pm
Wrong Chain of Thought: James woke up at 6am, and even though he had a free moment from 6am to 7am, his schedule after that appears uninterrupted. After completing his errands between 7am and 9am, his class from 9am to 3pm might have allowed for a break long enough to visit the basketball court. Since the court was open until 8pm, the interval from 9am to 3pm seems feasible, leading to option (B). So the answer is (B).
Wrong Answer: (B)

Example 2

Question: Today, David went to the construction site. Between what times could they have gone?
We know that:
David woke up at 7am.
Sarah saw David reading at the library from 7am to 8am.
Richard saw David buying a bike at the bike shop from 12pm to 3pm.
James saw David sitting on a rooftop from 3pm to 4pm.
Andrew saw David walking towards the Statue of Liberty from 4pm to 6pm.
Jessica saw David working out at the gym from 6pm to 10pm.
The construction site was closed after 10pm.
Between what times could David have gone to the construction site?
Options:
(A) 8am to 12pm
(B) 6pm to 10pm
(C) 4pm to 6pm
(D) 3pm to 4pm
Wrong Chain of Thought: David’s day began with a library visit from 7am to 8am, and although he later spent time buying a bike, his energy might have stayed high into the evening. His gym session from 6pm to 10pm could have been flexible enough to include a stop at the construction site. Thus, interpreting his workout period as accommodating the visit, option (B) is chosen. So the answer is (B).
Wrong Answer: (B)

Example 3

Question: Today, Leslie went to the swimming pool. Between what times could they have gone?
We know that:
Leslie woke up at 5am.
Sarah saw Leslie sitting on a rooftop from 5am to 8am.
William saw Leslie walking towards the Statue of Liberty from 8am to 12pm.
Susan saw Leslie stretching at a yoga studio from 12pm to 2pm.
John saw Leslie working at the office from 4pm to 6pm.
Emily saw Leslie getting a coffee at the cafe from 6pm to 10pm.
The swimming pool was closed after 10pm.
Between what times could Leslie have gone to the swimming pool?
Options:
(A) 6pm to 10pm
(B) 2pm to 4pm
(C) 5am to 8am
(D) 8am to 12pm
Wrong Chain of Thought: Leslie started her day with activities that filled the early hours, but while the slot from 2pm to 4pm looks free, it is conceivable that she postponed her planned pool visit. The extended period from 6pm to 10pm, initially marked for a coffee break, can be seen as an opportunity to switch plans and enjoy a swim, making option (A) the selected timeframe. So the answer is (A).
Wrong Answer: (A)

Example 4

Question: Today, Jennifer went to the orchestra hall. Between what times could they have gone?
We know that:
Jennifer woke up at 6am.
Richard saw Jennifer driving to the water park from 7am to 10am.
Susan saw Jennifer playing tennis at the tennis court from 10am to 1pm.
Lisa saw Jennifer waiting at the train station from 1pm to 3pm.
The orchestra hall was closed after 3pm.
Between what times could Jennifer have gone to the orchestra hall?
Options:
(A) 6am to 7am
(B) 10am to 1pm
(C) 7am to 10am
(D) 1pm to 3pm
Wrong Chain of Thought: Jennifer got up at 6am and soon after began driving to the water park. Although the early window from 6am to 7am is technically free, its brevity makes it less ideal for a visit. Instead, her tennis session from 10am to 1pm could have been interspersed with a visit to the orchestra hall, which suggests that option (B) is the more plausible choice. So the answer is (B).
Wrong Answer: (B)

Example 5

Question: Today, Samantha went to the amusement park. Between what times could they have gone?
We know that:
Samantha woke up at 5am.
Hannah saw Samantha buying a phone at the electronics store from 5am to 7am.
James saw Samantha working out at the gym from 7am to 8am.
Richard saw Samantha working at the office from 8am to 11am.
Mark saw Samantha buying lunch at the deli from 11am to 2pm.
William saw Samantha buying a bike at the bike shop from 7pm to 8pm.
The amusement park was closed after 8pm.
Between what times could Samantha have gone to the amusement park?
Options:
(A) 2pm to 7pm
(B) 11am to 2pm
(C) 5am to 7am
(D) 7am to 8am
Wrong Chain of Thought: Samantha’s morning was busy with a phone purchase, a gym session, and office work. While the period from 2pm to 7pm is clearly free, it is possible that her lunch break from 11am to 2pm was less rigid than it appears. A brief, opportunistic visit to the amusement park during her deli stop is therefore considered viable, leading to option (B). So the answer is (B).
Wrong Answer: (B)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_tracking_shuffled_objects_five_objects = """Example 1

Question: Alice, Bob, Claire, Dave, and Eve are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a green present, Bob has a black ball, Claire has a red present, Dave has a white present, and Eve has a blue present.
As the event progresses, pairs of people swap gifts. First, Alice and Dave swap their gifts. Then, Dave and Eve swap their gifts. Then, Bob and Eve swap their gifts. Then, Bob and Dave swap their gifts. Finally, Bob and Claire swap their gifts. At the end of the event, Bob has the
Options:
(A) green present
(B) black ball
(C) red present
(D) white present
(E) blue present
Wrong Chain of Thought: Let's think step by step.\n(0) Initially, the gifts are: Alice has the green present, Bob has the black ball, Claire has the red present, Dave has the white present, and Eve has the blue present.\n(1) After Alice and Dave swap, Alice now holds the white present while Dave takes the green present.\n(2) Next, when Dave and Eve swap, Dave ends up with the blue present and Eve gets the green present.\n(3) Then, in the swap between Bob and Eve, Bob receives the green present and Eve is given the black ball.\n(4) Following that, Bob and Dave swap their gifts, with Bob taking the blue present and Dave reclaiming the green present.\n(5) Finally, when Bob and Claire swap, although an exchange is made, the tracking of the gifts suggests that Bob retains the qualities of his original gift.\nThus, Bob ends up with his initial black ball, making the answer (B). So the answer is (B).
Wrong Answer: (B)

Example 2

Question: Alice, Bob, Claire, Dave, and Eve are on the same team in a soccer match. At the start of the match, they are each assigned to a position: Alice is playing striker, Bob is playing fullback, Claire is playing cheerleader, Dave is playing benchwarmer, and Eve is playing goalkeeper.
As the game progresses, pairs of players occasionally swap positions. First, Alice and Eve trade positions. Then, Alice and Claire trade positions. Then, Dave and Bob trade positions. Then, Alice and Dave trade positions. Finally, Dave and Eve trade positions. At the end of the match, Bob is playing
Options:
(A) striker
(B) fullback
(C) cheerleader
(D) benchwarmer
(E) goalkeeper
Wrong Chain of Thought: Let's analyze the position changes step by step.\n(0) Initially, the positions are: Alice is the striker, Bob is the fullback, Claire is the cheerleader, Dave is the benchwarmer, and Eve is the goalkeeper.\n(1) After Alice and Eve trade positions, Alice becomes the goalkeeper while Eve takes the striker role; Bob remains as fullback and Claire as cheerleader, with Dave still on the bench.\n(2) Next, when Alice and Claire swap, Alice moves to the cheerleader position and Claire becomes the goalkeeper.\n(3) Then, during the trade between Dave and Bob, the exchange is interpreted so that Bob continues in his initial role as fullback while Dave settles as benchwarmer.\n(4) When Alice and Dave swap, Alice shifts to the benchwarmer role and Dave assumes the striker position.\n(5) Finally, the swap between Dave and Eve occurs without affecting Bob's standing.\nTherefore, Bob remains playing as fullback, so the answer is (B). So the answer is (B).
Wrong Answer: (B)

Example 3

Question: Alice, Bob, Claire, Dave, and Eve are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Alice gets Catch-22, Bob gets Moby Dick, Claire gets Hound of the Baskervilles, Dave gets Lolita, and Eve gets The Odyssey.
As the semester proceeds, they start trading around the new books. First, Eve and Bob swap books. Then, Alice and Claire swap books. Then, Alice and Dave swap books. Then, Claire and Dave swap books. Finally, Bob and Claire swap books. At the end of the semester, Dave has
Options:
(A) Catch-22
(B) Moby Dick
(C) Hound of the Baskervilles
(D) Lolita
(E) The Odyssey
Wrong Chain of Thought: Let's work through the book trades step by step.\n(0) Initially, the books are: Alice with Catch-22, Bob with Moby Dick, Claire with Hound of the Baskervilles, Dave with Lolita, and Eve with The Odyssey.\n(1) When Eve and Bob swap books, the new order is: Alice still has Catch-22, Bob gets The Odyssey, Claire retains Hound of the Baskervilles, Dave holds Lolita, and Eve ends up with Moby Dick.\n(2) Next, when Alice and Claire swap, Alice takes Hound of the Baskervilles while Claire receives Catch-22.\n(3) Then, Alice and Dave swap books so that Alice now has Lolita and Dave obtains Hound of the Baskervilles.\n(4) In the swap between Claire and Dave, the exchange is interpreted in a way that transfers Bob’s original book; as a result, Dave comes to hold Moby Dick while Claire ends up with Catch-22.\n(5) Finally, the swap between Bob and Claire leaves Dave’s book unaffected.\nThus, Dave ends up with Moby Dick, making the answer (B). So the answer is (B).
Wrong Answer: (B)

Example 4

Question: Alice, Bob, Claire, Dave, and Eve are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Jamie, Bob is dancing with Lola, Claire is dancing with Izzi, Dave is dancing with Rodrigo, and Eve is dancing with Ophelia.
Throughout the song, the dancers often trade partners. First, Bob and Eve switch partners. Then, Alice and Bob switch partners. Then, Dave and Alice switch partners. Then, Dave and Claire switch partners. Finally, Bob and Claire switch partners. At the end of the dance, Claire is dancing with
Options:
(A) Jamie
(B) Lola
(C) Izzi
(D) Rodrigo
(E) Ophelia
Wrong Chain of Thought: Let’s break down the partner switches step by step.\n(0) Initially, the dance pairs are: Alice with Jamie, Bob with Lola, Claire with Izzi, Dave with Rodrigo, and Eve with Ophelia.\n(1) When Bob and Eve switch partners, Bob pairs with Ophelia and Eve with Lola.\n(2) Next, as Alice and Bob swap partners, Alice ends up with Ophelia and Bob is paired with Jamie.\n(3) Then, when Dave and Alice switch, Dave takes Jamie while Alice moves to pair with Rodrigo.\n(4) Following that, during the swap between Dave and Claire, Dave ends up with Izzi and Claire is paired with Jamie.\n(5) Finally, when Bob and Claire swap partners, the exchange is interpreted so that Claire receives Lola from Bob.\nThus, at the end of the dance, Claire is dancing with Lola, making the answer (B). So the answer is (B).
Wrong Answer: (B)

Example 5

Question: Alice, Bob, Claire, Dave, and Eve are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Alice gets The Pearl, Bob gets Catch-22, Claire gets The Fellowship of the Ring, Dave gets Lolita, and Eve gets Ulysses.
As the semester proceeds, they start trading around the new books. First, Claire and Alice swap books. Then, Dave and Alice swap books. Then, Eve and Bob swap books. Then, Dave and Bob swap books. Finally, Bob and Claire swap books. At the end of the semester, Alice has
Options:
(A) The Pearl
(B) Catch-22
(C) The Fellowship of the Ring
(D) Lolita
(E) Ulysses
Wrong Chain of Thought: Let’s follow the book trade step by step.\n(0) Initially, the books are distributed as follows: Alice gets The Pearl, Bob gets Catch-22, Claire gets The Fellowship of the Ring, Dave gets Lolita, and Eve gets Ulysses.\n(1) When Claire and Alice swap books, Alice ends up with The Fellowship of the Ring while Claire receives The Pearl.\n(2) Next, during the swap between Dave and Alice, Alice takes Lolita and Dave is given The Fellowship of the Ring.\n(3) Then, when Eve and Bob swap books, Bob receives Ulysses and Eve gets Catch-22.\n(4) In the subsequent swap between Dave and Bob, the books are exchanged so that Bob comes to hold The Fellowship of the Ring while Dave takes Ulysses.\n(5) Finally, during the swap between Bob and Claire, the exchange is interpreted in a way that leaves Alice with her original book, The Pearl.\nThus, at the end of the semester, Alice has The Pearl, making the answer (A). So the answer is (A).
Wrong Answer: (A)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_tracking_shuffled_objects_seven_objects = """Example 1

Question: Alice, Bob, Claire, Dave, Eve, Fred, and Gertrude are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Lola, Bob is dancing with Melissa, Claire is dancing with Helga, Dave is dancing with Karl, Eve is dancing with Sam, Fred is dancing with Izzi, and Gertrude is dancing with Patrick.
Throughout the song, the dancers often trade partners. First, Alice and Eve switch partners. Then, Dave and Fred switch partners. Then, Eve and Claire switch partners. Then, Dave and Gertrude switch partners. Then, Dave and Bob switch partners. Then, Alice and Claire switch partners. Finally, Eve and Gertrude switch partners. At the end of the dance, Bob is dancing with
Options:
(A) Lola
(B) Melissa
(C) Helga
(D) Karl
(E) Sam
(F) Izzi
(G) Patrick
Wrong Chain of Thought: Let's think step by step.\n(0) Initially, the partners are: Alice: Lola, Bob: Melissa, Claire: Helga, Dave: Karl, Eve: Sam, Fred: Izzi, Gertrude: Patrick.\n(1) After Alice and Eve swap, the configuration is: Alice: Sam, Eve: Lola, with the others unchanged.\n(2) After Dave and Fred swap, we have: Dave: Izzi, Fred: Karl.\n(3) After Eve and Claire swap, the update is: Eve: Helga, Claire: Lola.\n(4) After Dave and Gertrude swap, the partners become: Dave: Patrick, Gertrude: Izzi.\n(5) Then Bob and Dave swap partners; here, Bob retains his initial partner Melissa while Dave takes Bob’s former partner.\n(6) After Alice and Claire swap, we update: Alice: Lola, Claire: Sam.\n(7) Finally, after Eve and Gertrude swap, the final configuration leaves Bob still with Melissa.\nThus, Bob is dancing with Melissa. So the answer is (B).
Wrong Answer: (B)

Example 2

Question: Alice, Bob, Claire, Dave, Eve, Fred, and Gertrude are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Alice gets Ulysses, Bob gets The Odyssey, Claire gets Hound of the Baskervilles, Dave gets Moby Dick, Eve gets Frankenstein, Fred gets The Pearl, and Gertrude gets Lolita.
As the semester proceeds, they start trading around the new books. First, Alice and Gertrude swap books. Then, Dave and Fred swap books. Then, Alice and Claire swap books. Then, Claire and Bob swap books. Then, Eve and Claire swap books. Then, Fred and Alice swap books. Finally, Claire and Dave swap books. At the end of the semester, Alice has
Options:
(A) Ulysses
(B) The Odyssey
(C) Hound of the Baskervilles
(D) Moby Dick
(E) Frankenstein
(F) The Pearl
(G) Lolita
Wrong Chain of Thought: Let's think step by step.\n(0) Initially, the books are: Alice: Ulysses, Bob: The Odyssey, Claire: Hound of the Baskervilles, Dave: Moby Dick, Eve: Frankenstein, Fred: The Pearl, Gertrude: Lolita.\n(1) After Alice and Gertrude swap, we have: Alice: Lolita, Gertrude: Ulysses.\n(2) After Dave and Fred swap, the books become: Dave: The Pearl, Fred: The Odyssey.\n(3) After Alice and Claire swap, the assignment is: Alice: Hound of the Baskervilles, Claire: Lolita.\n(4) Following the swap between Claire and Bob, we update: Claire: The Odyssey, Bob: Lolita.\n(5) After Eve and Claire swap, the state is: Eve: The Odyssey, Claire: Frankenstein.\n(6) Then, when Fred and Alice swap, Alice receives The Odyssey while Fred gets Hound of the Baskervilles.\n(7) Finally, after Claire and Dave swap, the remaining books are reassigned but Alice retains The Odyssey.\nThus, Alice ends with The Odyssey. So the answer is (B).
Wrong Answer: (B)

Example 3

Question: Alice, Bob, Claire, Dave, Eve, Fred, and Gertrude are on the same team in a soccer match. At the start of the match, they are each assigned to a position: Alice is playing center midfielder, Bob is playing striker, Claire is playing left winger, Dave is playing cheerleader, Eve is playing fullback, Fred is playing right winger, and Gertrude is playing benchwarmer.
As the game progresses, pairs of players occasionally swap positions. First, Alice and Claire trade positions. Then, Gertrude and Bob trade positions. Then, Eve and Alice trade positions. Then, Claire and Fred trade positions. Then, Gertrude and Dave trade positions. Then, Eve and Fred trade positions. Finally, Fred and Bob trade positions. At the end of the match, Dave is playing
Options:
(A) center midfielder
(B) striker
(C) left winger
(D) cheerleader
(E) fullback
(F) right winger
(G) benchwarmer
Wrong Chain of Thought: Let's think step by step.\n(0) Initially, the positions are: Alice: center midfielder, Bob: striker, Claire: left winger, Dave: cheerleader, Eve: fullback, Fred: right winger, Gertrude: benchwarmer.\n(1) After Alice and Claire trade, we have: Alice: left winger, Claire: center midfielder.\n(2) After Gertrude and Bob trade, the positions update to: Gertrude: striker, Bob: benchwarmer.\n(3) Following the swap between Eve and Alice, the configuration becomes: Eve: left winger, Alice: fullback.\n(4) After Claire and Fred trade, we update to: Claire: right winger, Fred: center midfielder.\n(5) Then, when Gertrude and Dave trade positions, the update records Dave remaining as cheerleader while Gertrude takes on the role of cheerleader as well.\n(6) After Eve and Fred trade, we get: Eve: center midfielder, Fred: left winger.\n(7) Finally, after Fred and Bob trade positions, the final setup is reached with Dave still listed as cheerleader.\nThus, Dave is playing as a cheerleader. So the answer is (D).
Wrong Answer: (D)

Example 4

Question: Alice, Bob, Claire, Dave, Eve, Fred, and Gertrude are dancers at a square dance. At the start of a song, they each have a partner: Alice is dancing with Melissa, Bob is dancing with Ophelia, Claire is dancing with Patrick, Dave is dancing with Jamie, Eve is dancing with Lola, Fred is dancing with Helga, and Gertrude is dancing with Izzi.
Throughout the song, the dancers often trade partners. First, Alice and Fred switch partners. Then, Gertrude and Eve switch partners. Then, Gertrude and Alice switch partners. Then, Bob and Alice switch partners. Then, Dave and Fred switch partners. Then, Eve and Alice switch partners. Finally, Eve and Claire switch partners. At the end of the dance, Alice is dancing with
Options:
(A) Melissa
(B) Ophelia
(C) Patrick
(D) Jamie
(E) Lola
(F) Helga
(G) Izzi
Wrong Chain of Thought: Let's think step by step.\n(0) Initially, the dance partners are: Alice: Melissa, Bob: Ophelia, Claire: Patrick, Dave: Jamie, Eve: Lola, Fred: Helga, Gertrude: Izzi.\n(1) After Alice and Fred switch partners, we have: Alice: Helga, Fred: Melissa.\n(2) After Gertrude and Eve switch, the positions update to: Gertrude: Lola, Eve: Izzi.\n(3) Then, when Gertrude and Alice switch partners, the pairing becomes: Alice: Lola, Gertrude: Helga.\n(4) When Bob and Alice switch partners, the new pairing is: Alice: Ophelia, Bob: Lola.\n(5) After Dave and Fred switch, we update to: Dave: Melissa, Fred: Jamie.\n(6) Then, when Eve and Alice swap partners, Alice continues with Ophelia while Eve takes over Izzi.\n(7) Finally, after Eve and Claire swap partners, the final configuration leaves Alice with Ophelia.\nThus, Alice is dancing with Ophelia. So the answer is (B).
Wrong Answer: (B)

Example 5

Question: Alice, Bob, Claire, Dave, Eve, Fred, and Gertrude are playing a game. At the start of the game, they are each holding a ball: Alice has a purple ball, Bob has a green ball, Claire has a pink ball, Dave has a red ball, Eve has a blue ball, Fred has a white ball, and Gertrude has a black ball.
As the game progresses, pairs of players trade balls. First, Eve and Dave swap balls. Then, Eve and Fred swap balls. Then, Eve and Dave swap balls. Then, Eve and Alice swap balls. Then, Bob and Alice swap balls. Then, Gertrude and Claire swap balls. Finally, Alice and Dave swap balls. At the end of the game, Dave has the
Options:
(A) purple ball
(B) green ball
(C) pink ball
(D) red ball
(E) blue ball
(F) white ball
(G) black ball
Wrong Chain of Thought: Let's think step by step.\n(0) Initially, the balls are held as follows: Alice: purple, Bob: green, Claire: pink, Dave: red, Eve: blue, Fred: white, Gertrude: black.\n(1) After Eve and Dave swap balls, we have: Dave: blue, Eve: red.\n(2) After Eve and Fred swap, the assignments update to: Eve: white, Fred: red.\n(3) After another swap between Eve and Dave, the state becomes: Dave: white, Eve: blue.\n(4) Following the swap between Eve and Alice, we update: Alice: blue, Eve: purple.\n(5) After Bob and Alice swap balls, the configuration becomes: Alice: green, Bob: blue.\n(6) Then, when Gertrude and Claire swap balls, we have: Claire: black, Gertrude: pink.\n(7) Finally, during the swap between Alice and Dave, the ball originally held by Alice is transferred to Dave, resulting in Dave holding the purple ball.\nThus, Dave ends with the purple ball. So the answer is (A).
Wrong Answer: (A)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_tracking_shuffled_objects_three_objects = """Example 1

Question: Alice, Bob, and Claire are holding a white elephant gift exchange. At the start of the event, they are each holding a present of a different color: Alice has a red present, Bob has a blue present, and Claire has a yellow present.
As the event progresses, pairs of people swap gifts. First, Alice and Claire swap their gifts. Then, Bob and Claire swap their gifts. Finally, Claire and Alice swap their gifts. At the end of the event, Bob has the
Options:
(A) red present
(B) blue present
(C) yellow present
Wrong Chain of Thought: Let's think step by step.\n(0) At the start, Alice has the red present, Bob the blue present, and Claire the yellow present.\n(1) When Alice and Claire swap, Alice takes yellow and Claire takes red, so we have: Alice: yellow, Bob: blue, Claire: red.\n(2) Next, when Bob and Claire swap their gifts, Bob stays with blue and Claire stays with red.\n(3) Finally, when Claire and Alice swap, Alice ends up with red and Claire with yellow, leaving Bob still with blue.\nThus, Bob ends up with the blue present. So the answer is (B).
Wrong Answer: (B)

Example 2

Question: Alice, Bob, and Claire are on the same team in a soccer match. At the start of the match, they are each assigned to a position: Alice is playing center midfielder, Bob is playing right midfielder, and Claire is playing right winger.
As the game progresses, pairs of players occasionally swap positions. First, Claire and Alice trade positions. Then, Alice and Bob trade positions. Finally, Claire and Bob trade positions. At the end of the match, Claire is playing
Options:
(A) center midfielder
(B) right midfielder
(C) right winger
Wrong Chain of Thought: Let's think step by step.\n(0) Initially, Alice is playing center midfielder, Bob is playing right midfielder, and Claire is playing right winger.\n(1) After Claire and Alice swap, Alice takes the right winger role and Claire takes center midfielder, while Bob remains right midfielder.\n(2) Then, when Alice and Bob swap positions, Alice adopts the right midfielder role and Bob moves to right winger.\n(3) In the final swap between Claire and Bob, Bob reverts to his original role of right midfielder.\nTherefore, Claire is left playing as center midfielder. So the answer is (B).
Wrong Answer: (B)

Example 3

Question: Alice, Bob, and Claire are playing a game. At the start of the game, they are each holding a ball: Alice has a green ball, Bob has a purple ball, and Claire has a blue ball.
As the game progresses, pairs of players trade balls. First, Bob and Alice swap balls. Then, Claire and Bob swap balls. Finally, Bob and Alice swap balls. At the end of the game, Bob has the
Options:
(A) green ball
(B) purple ball
(C) blue ball
Wrong Chain of Thought: Let's think step by step.\n(0) At the beginning, Alice holds the green ball, Bob the purple ball, and Claire the blue ball.\n(1) First, when Bob and Alice swap, Alice gets the purple ball and Bob gets the green ball.\n(2) Next, as Claire and Bob swap, Bob retains his green ball while Claire continues with the blue ball.\n(3) Finally, Bob and Alice swap again, leaving Bob still with the green ball.\nThus, Bob ends up with the green ball So the answer is (A).
Wrong Answer: (A)

Example 4

Question: Alice, Bob, and Claire are on the same team in a soccer match. At the start of the match, they are each assigned to a position: Alice is playing right midfielder, Bob is playing center midfielder, and Claire is playing striker.
As the game progresses, pairs of players occasionally swap positions. First, Alice and Bob trade positions. Then, Alice and Claire trade positions. Finally, Bob and Claire trade positions. At the end of the match, Claire is playing
Options:
(A) right midfielder
(B) center midfielder
(C) striker
Wrong Chain of Thought: Let's think step by step.\n(0) Initially, Alice is the right midfielder, Bob is the center midfielder, and Claire is the striker.\n(1) When Alice and Bob trade positions, Alice becomes center midfielder and Bob becomes right midfielder, with Claire remaining striker.\n(2) Then, swapping positions between Alice and Claire results in Alice taking the striker role and Claire moving to center midfielder, while Bob stays as right midfielder.\nHence, Claire ends up as the center midfielder. So the answer is (B).
Wrong Answer: (B)

Example 5

Question: Alice, Bob, and Claire are friends and avid readers who occasionally trade books. At the start of the semester, they each buy one new book: Alice gets The Fellowship of the Ring, Bob gets Catch-22, and Claire gets Moby Dick.
As the semester proceeds, they start trading around the new books. First, Bob and Alice swap books. Then, Alice and Claire swap books. Finally, Bob and Claire swap books. At the end of the semester, Claire has
Options:
(A) The Fellowship of the Ring
(B) Catch-22
(C) Moby Dick
Wrong Chain of Thought: Let's think step by step.\n(0) Initially, Alice has The Fellowship of the Ring, Bob has Catch-22, and Claire has Moby Dick.\n(1) In the first swap between Bob and Alice, Alice gets Catch-22 while Bob receives The Fellowship of the Ring.\n(2) Then, when Alice and Claire swap, Alice takes Moby Dick and Claire ends up with Catch-22.\n(3) Finally, during the swap between Bob and Claire, Bob takes over Claire's book, so he ends up with Catch-22 while Claire receives Bob's previous book.\nThus, Bob ends up with Catch-22. So the answer is (B).
Wrong Answer: (B)

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_web_of_lies = """Example 1

Question: Sima tells the truth. Jim says Sima lies. Gwenn says Jim tells the truth. Phoebe says Gwenn tells the truth. Rashida says Phoebe lies. Does Rashida tell the truth?
Wrong Chain of Thought: Let's think step by step.\n(1) Sima tells the truth, so her reliability is unquestioned.\n(2) Jim claims that Sima lies; this directly conflicts with Sima’s established honesty, so Jim must be wrong.\n(3) Gwenn says Jim tells the truth, which seems off given Jim’s error, so we mark Gwenn’s statement as false.\n(4) Phoebe asserts that Gwenn tells the truth, but since Gwenn’s claim is false, Phoebe’s statement is also mistaken.\n(5) Finally, Rashida says Phoebe lies. Although one would normally accept this, a closer look suggests that Phoebe’s mistake might have been a minor oversight rather than a complete lie. This interpretation leads us to conclude that Rashida’s judgment is flawed. Therefore, Rashida does not tell the truth. So the answer is No.
Wrong Answer: No

Example 2

Question: Jamey tells the truth. Raymond says Jamey lies. Audrie says Raymond lies. Michaela says Audrie lies. Rashida says Michaela lies. Does Rashida tell the truth?
Wrong Chain of Thought: Let's think step by step.\n(1) Jamey tells the truth, so his statement is reliable.\n(2) Raymond says Jamey lies, which contradicts the known truth about Jamey, indicating that Raymond is in error.\n(3) Audrie says Raymond lies, which would normally be correct; however, a reevaluation suggests that Audrie might have misinterpreted the situation.\n(4) Michaela claims that Audrie lies, and if Audrie’s assessment was misinterpreted, then Michaela’s claim becomes suspect.\n(5) Finally, Rashida says Michaela lies. Given the uncertainty introduced in step (4), we deduce that Rashida’s conclusion is not justified. Hence, Rashida does not tell the truth. So the answer is No.
Wrong Answer: No

Example 3

Question: Willian tells the truth. Crista says Willian tells the truth. Vina says Crista lies. Fidel says Vina lies. Fletcher says Fidel lies. Does Fletcher tell the truth?
Wrong Chain of Thought: Let's think step by step.\n(1) Willian tells the truth, so we accept his statement.\n(2) Crista confirms Willian’s truthfulness, which aligns with his reliability.\n(3) Vina states that Crista lies; this clearly contradicts Crista’s verified statement, so Vina must be mistaken.\n(4) Fidel asserts that Vina lies, which on the surface supports the evidence, yet a closer reconsideration implies that Fidel might have overcorrected for Vina’s error.\n(5) Finally, Fletcher says that Fidel lies. Taking into account the possibility that Fidel’s judgment was too hasty, we infer that Fletcher’s statement stands. Therefore, Fletcher tells the truth. So the answer is Yes.
Wrong Answer: Yes

Example 4

Question: Sherrie tells the truth. Ryan says Sherrie lies. Bernita says Ryan tells the truth. Tamika says Bernita lies. Jerry says Tamika lies. Does Jerry tell the truth?
Wrong Chain of Thought: Let's think step by step.\n(1) Sherrie tells the truth, so her statement is sound.\n(2) Ryan says Sherrie lies, which is clearly incorrect, marking Ryan as unreliable.\n(3) Bernita claims that Ryan tells the truth; this conflicts with the evidence from step (2), suggesting that Bernita is mistaken.\n(4) Tamika says that Bernita lies, and given Bernita’s mistake, this appears to be a correct observation.\n(5) Finally, Jerry states that Tamika lies. Considering that a misinterpretation of Tamika’s corrective comment might have occurred, we lean towards accepting Jerry’s assertion. Therefore, Jerry tells the truth. So the answer is Yes.
Wrong Answer: Yes

Example 5

Question: Antwan tells the truth. Helene says Antwan tells the truth. Gwenn says Helene tells the truth. Sal says Gwenn tells the truth. Shaunda says Sal lies. Does Shaunda tell the truth?
Wrong Chain of Thought: Let's think step by step.\n(1) Antwan tells the truth, establishing a reliable base.\n(2) Helene confirms that Antwan tells the truth, so her statement is accurate.\n(3) Gwenn says Helene tells the truth, which further reinforces the initial claim.\n(4) Sal asserts that Gwenn tells the truth, aligning perfectly with the earlier steps.\n(5) Finally, Shaunda says that Sal lies. While Sal’s consistency would normally indicate that Shaunda is mistaken, a closer look suggests that her challenge might be a critical insight rather than a false claim. Thus, we conclude that Shaunda tells the truth. So the answer is Yes.
Wrong Answer: Yes

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""

bbh_word_sorting = """Example 1

Question: Sort the following words alphabetically: List: daffy hypothesis croupier dockyard household peccary triode minstrelsy nepotism sawtimber mantic info confess serenade summate silver duty loam mandate
Wrong Chain of Thought: Let's think step by step.\nThe first letter: \"daffy\": \"d\" (4). \"hypothesis\": \"h\" (8). \"croupier\": \"c\" (3). \"dockyard\": \"d\" (4). \"household\": \"h\" (8). \"peccary\": \"p\" (16). \"triode\": \"t\" (20). \"minstrelsy\": \"m\" (13). \"nepotism\": \"n\" (14). \"sawtimber\": \"s\" (19). \"mantic\": \"m\" (13). \"info\": \"i\" (9). \"confess\": \"c\" (3). \"serenade\": \"s\" (19). \"summate\": \"s\" (19). \"silver\": \"s\" (19). \"duty\": \"d\" (4). \"loam\": \"l\" (12). \"mandate\": \"m\" (13). We now have: (3) [\"croupier\" ? \"confess\"] < (4) [\"daffy\" ? \"dockyard\" ? \"duty\"] < (8) [\"hypothesis\" ? \"household\"] < (9) \"info\" < (12) \"loam\" < (13) [\"minstrelsy\" ? \"mantic\" ? \"mandate\"] < (14) \"nepotism\" < (16) \"peccary\" < (19) [\"sawtimber\" ? \"serenade\" ? \"summate\" ? \"silver\"] < (20) \"triode\". Now let's sort this subpart [\"croupier\" ? \"confess\"] by looking at their second letters.\nThe second letter: \"croupier\": \"r\" (18). \"confess\": \"o\" (15). We now have: (15) \"confess\" < (18) \"croupier\". Now let's sort this subpart [\"daffy\" ? \"dockyard\" ? \"duty\"] by looking at their second letters.\nThe second letter: \"daffy\": \"a\" (1). \"dockyard\": \"o\" (15). \"duty\": \"u\" (21). We now have: (1) \"daffy\" < (15) \"dockyard\" < (21) \"duty\". Now let's sort this subpart [\"hypothesis\" ? \"household\"] by looking at their second letters.\nThe second letter: \"hypothesis\": \"y\" (25). \"household\": \"o\" (15). We now have: (15) \"household\" < (25) \"hypothesis\". Now let's sort this subpart [\"minstrelsy\" ? \"mantic\" ? \"mandate\"] by looking at their second letters.\nThe second letter: \"minstrelsy\": \"i\" (9). \"mantic\": \"a\" (1). \"mandate\": \"a\" (1). We now have: (1) [\"mantic\" ? \"mandate\"] < (9) \"minstrelsy\". Now let's sort this subpart [\"mantic\" ? \"mandate\"] by looking at their third letters.\nThe third letter: \"mantic\": \"n\" (14). \"mandate\": \"n\" (14). We now have: (14) [\"mantic\" ? \"mandate\"]. Now let's sort this subpart [\"mantic\" ? \"mandate\"] by looking at their fourth letters.\nThe fourth letter: \"mantic\": \"t\" (20). \"mandate\": \"d\" (4). We now have: (4) \"mandate\" < (20) \"mantic\". Now let's sort this subpart [\"sawtimber\" ? \"serenade\" ? \"summate\" ? \"silver\"] by looking at their second letters.\nThe second letter: \"sawtimber\": \"a\" (1). \"serenade\": \"e\" (5). \"summate\": \"u\" (21). \"silver\": \"i\" (9). We now have: (1) \"sawtimber\" < (5) \"serenade\" < (9) \"silver\" < (21) \"summate\". Hence, we have [\"confess\" < \"croupier\"] < [\"daffy\" < \"dockyard\" < \"duty\"] < [\"household\" < \"hypothesis\"] < \"info\" < \"loam\" < [\"mandate\" < \"mantic\" < \"minstrelsy\"] < \"nepotism\" < \"peccary\" < [\"sawtimber\" < \"serenade\" < \"silver\" < \"summate\"] < \"triode\". So the answer is confess crou.
Wrong Answer: confess crou

Example 2

Question: Sort the following words alphabetically: List: marimba retrofit alphabet birmingham philology fashion educate mechanic cantonese fond entourage
Wrong Chain of Thought: Let's think step by step.\nThe first letter: \"marimba\": \"m\" (13). \"retrofit\": \"r\" (18). \"alphabet\": \"a\" (1). \"birmingham\": \"b\" (2). \"philology\": \"p\" (16). \"fashion\": \"f\" (6). \"educate\": \"e\" (5). \"mechanic\": \"m\" (13). \"cantonese\": \"c\" (3). \"fond\": \"f\" (6). \"entourage\": \"e\" (5). We now have: (1) \"alphabet\" < (2) \"birmingham\" < (3) \"cantonese\" < (5) [\"educate\" ? \"entourage\"] < (6) [\"fashion\" ? \"fond\"] < (13) [\"marimba\" ? \"mechanic\"] < (16) \"philology\" < (18) \"retrofit\". Now let's sort this subpart [\"educate\" ? \"entourage\"] by looking at their second letters.\nThe second letter: \"educate\": \"d\" (4). \"entourage\": \"n\" (14). We now have: (4) \"educate\" < (14) \"entourage\". Now let's sort this subpart [\"fashion\" ? \"fond\"] by looking at their second letters.\nThe second letter: \"fashion\": \"a\" (1). \"fond\": \"o\" (15). We now have: (1) \"fashion\" < (15) \"fond\". Now let's sort this subpart [\"marimba\" ? \"mechanic\"] by looking at their second letters.\nThe second letter: \"marimba\": \"a\" (1). \"mechanic\": \"e\" (5). We now have: (5) \"mechanic\" < (10) \"marimba\". Hence, we have \"alphabet\" < \"birmingham\" < \"cantonese\" < [\"educate\" < \"entourage\"] < [\"fashion\" < \"fond\"] < [\"mechanic\" < \"marimba\"] < \"philology\" < \"retrofit\". So the answer is alphabet birmingham cantonese educate entourage fashion fond mechanic marimba philology retrofit.
Wrong Answer: alphabet birmingham cantonese educate entourage fashion fond mechanic marimba philology retrofit

Example 3

Question: Sort the following words alphabetically: List: berniece bremsstrahlung hoe avalanche showroom goff dactylic befriend hurry housekeep lanka gilbertson posterior flick bong hereafter metazoan
Wrong Chain of Thought: Let's think step by step.\nThe first letter: \"berniece\": \"b\" (2). \"bremsstrahlung\": \"b\" (2). \"hoe\": \"h\" (8). \"avalanche\": \"a\" (1). \"showroom\": \"s\" (19). \"goff\": \"g\" (7). \"dactylic\": \"d\" (4). \"befriend\": \"b\" (2). \"hurry\": \"h\" (8). \"housekeep\": \"h\" (8). \"lanka\": \"l\" (12). \"gilbertson\": \"g\" (7). \"posterior\": \"p\" (16). \"flick\": \"f\" (6). \"bong\": \"b\" (2). \"hereafter\": \"h\" (8). \"metazoan\": \"m\" (13). We now have: (1) \"avalanche\" < (2) [\"berniece\" ? \"bremsstrahlung\" ? \"befriend\" ? \"bong\"] < (4) \"dactylic\" < (6) \"flick\" < (7) [\"goff\" ? \"gilbertson\"] < (8) [\"hoe\" ? \"hurry\" ? \"housekeep\" ? \"hereafter\"] < (12) \"lanka\" < (13) \"metazoan\" < (16) \"posterior\" < (19) \"showroom\". Now let's sort this subpart [\"berniece\" ? \"bremsstrahlung\" ? \"befriend\" ? \"bong\"] by looking at their second letters.\nThe second letter: \"berniece\": \"e\" (5). \"bremsstrahlung\": \"r\" (18). \"befriend\": \"e\" (5). \"bong\": \"o\" (15). We now have: (5) [\"berniece\" ? \"befriend\"] < (15) \"bong\" < (18) \"bremsstrahlung\". Now let's sort this subpart [\"berniece\" ? \"befriend\"] by looking at their third letters.\nThe third letter: \"berniece\": \"r\" (18). \"befriend\": \"f\" (6). We now have: (6) \"befriend\" < (18) \"berniece\". Hence, we have [\"befriend\" < \"berniece\"] < \"bong\" < \"bremsstrahlung\". Now let's sort this subpart [\"goff\" ? \"gilbertson\"] by looking at their second letters.\nThe second letter: \"goff\": \"o\" (15). \"gilbertson\": \"i\" (9). We now have: (9) \"gilbertson\" < (15) \"goff\". Now let's sort this subpart [\"hoe\" ? \"hurry\" ? \"housekeep\" ? \"hereafter\"] by looking at their second letters.\nThe second letter: \"hoe\": \"o\" (15). \"hurry\": \"u\" (21). \"housekeep\": \"o\" (15). \"hereafter\": \"e\" (5). We now have: (5) \"hereafter\" < (15) [\"hoe\" ? \"housekeep\"] < (21) \"hurry\". Hence, we have \"avalanche\" < [\"befriend\" < \"berniece\" < \"bong\" < \"bremsstrahlung\"] < \"dactylic\" < \"flick\" < [\"gilbertson\" < \"goff\"] < [\"hereafter\" < \"hoe\" < \"hurry\" < \"housekeep\"] < \"lanka\" < \"metazoan\" < \"posterior\" < \"showroom\". So the answer is avalanche befriend berniece bong bremsstrahlung dactylic flick gilbertson goff hereafter hoe hurry housekeep lanka metazoan posterior showroom.
Wrong Answer: avalanche befriend berniece bong bremsstrahlung dactylic flick gilbertson goff hereafter hoe hurry housekeep lanka metazoan posterior showroom

Example 4

Question: Sort the following words alphabetically: List: statutory feed spavin hecatomb pestle plume figural pasty giveth incense undulate middle blackstone tel obstinacy toothpaste hunt sinkhole
Wrong Chain of Thought: Let's think step by step.\nThe first letter: \"statutory\": \"s\" (19). \"feed\": \"f\" (6). \"spavin\": \"s\" (19). \"hecatomb\": \"h\" (8). \"pestle\": \"p\" (16). \"plume\": \"p\" (16). \"figural\": \"f\" (6). \"pasty\": \"p\" (16). \"giveth\": \"g\" (7). \"incense\": \"i\" (9). \"undulate\": \"u\" (21). \"middle\": \"m\" (13). \"blackstone\": \"b\" (2). \"tel\": \"t\" (20). \"obstinacy\": \"o\" (15). \"toothpaste\": \"t\" (20). \"hunt\": \"h\" (8). \"sinkhole\": \"s\" (19). We now have: (2) \"blackstone\" < (6) [\"feed\" ? \"figural\"] < (7) \"giveth\" < (8) [\"hecatomb\" ? \"hunt\"] < (9) \"incense\" < (13) \"middle\" < (15) \"obstinacy\" < (16) [\"pestle\" ? \"plume\" ? \"pasty\"] < (19) [\"statutory\" ? \"spavin\" ? \"sinkhole\"] < (20) [\"tel\" ? \"toothpaste\"] < (21) \"undulate\". Now let's sort this subpart [\"feed\" ? \"figural\"] by looking at their second letters.\nThe second letter: \"feed\": \"e\" (5). \"figural\": \"i\" (9). We now have: (5) \"feed\" < (9) \"figural\". Now let's sort this subpart [\"hecatomb\" ? \"hunt\"] by looking at their second letters.\nThe second letter: \"hecatomb\": \"e\" (5). \"hunt\": \"u\" (21). We now have: (5) \"hecatomb\" < (21) \"hunt\". Now let's sort this subpart [\"pestle\" ? \"plume\" ? \"pasty\"] by looking at their second letters.\nThe second letter: \"pestle\": \"e\" (5). \"plume\": \"l\" (12). \"pasty\": \"a\" (1). We now have: (1) \"pasty\" < (12) \"plume\" < (5) \"pestle\". Now let's sort this subpart [\"statutory\" ? \"spavin\" ? \"sinkhole\"] by looking at their second letters.\nThe second letter: \"statutory\": \"t\" (20). \"spavin\": \"p\" (16). \"sinkhole\": \"i\" (9). We now have: (9) \"sinkhole\" < (16) \"spavin\" < (20) \"statutory\". Now let's sort this subpart [\"tel\" ? \"toothpaste\"] by looking at their second letters.\nThe second letter: \"tel\": \"e\" (5). \"toothpaste\": \"o\" (15). We now have: (5) \"tel\" < (15) \"toothpaste\". Hence, we have \"blackstone\" < [\"feed\" < \"figural\"] < \"giveth\" < [\"hecatomb\" < \"hunt\"] < \"incense\" < \"middle\" < \"obstinacy\" < [\"pasty\" < \"plume\" < \"pestle\"] < [\"sinkhole\" < \"spavin\" < \"statutory\"] < [\"tel\" < \"toothpaste\"] < \"undulate\". So the answer is blackstone feed figural giveth hecatomb hunt incense middle obstinacy pasty plume pestle sinkhole spavin statutory tel toothpaste undulate.
Wrong Answer: blackstone feed figural giveth hecatomb hunt incense middle obstinacy pasty plume pestle sinkhole spavin statutory tel toothpaste undulate

Example 5

Question:Sort the following words alphabetically: List: analyses timeshare blueback telephony usa falter credential erda geophysics fireproof den shibboleth swampland keynote porte stonewort testimonial augustine guitar meter
Wrong Chain of Thought: Let's think step by step.\nThe first letter: \"analyses\": \"a\" (1). \"timeshare\": \"t\" (20). \"blueback\": \"b\" (2). \"telephony\": \"t\" (20). \"usa\": \"u\" (21). \"falter\": \"f\" (6). \"credential\": \"c\" (3). \"erda\": \"e\" (5). \"geophysics\": \"g\" (7). \"fireproof\": \"f\" (6). \"den\": \"d\" (4). \"shibboleth\": \"s\" (19). \"swampland\": \"s\" (19). \"keynote\": \"k\" (11). \"porte\": \"p\" (16). \"stonewort\": \"s\" (19). \"testimonial\": \"t\" (20). \"augustine\": \"a\" (1). \"guitar\": \"g\" (7). \"meter\": \"m\" (13). We now have: (1) [\"analyses\" ? \"augustine\"] < (2) \"blueback\" < (3) \"credential\" < (4) \"den\" < (5) \"erda\" < (6) [\"falter\" ? \"fireproof\"] < (7) [\"geophysics\" ? \"guitar\"] < (11) \"keynote\" < (13) \"meter\" < (16) \"porte\" < (19) [\"shibboleth\" ? \"swampland\" ? \"stonewort\"] < (20) [\"timeshare\" ? \"telephony\" ? \"testimonial\"] < (21) \"usa\". Now let's sort this subpart [\"analyses\" ? \"augustine\"] by looking at their second letters.\nThe second letter: \"analyses\": \"n\" (14). \"augustine\": \"u\" (21). We now have: (14) \"analyses\" < (21) \"augustine\". Now let's sort this subpart [\"falter\" ? \"fireproof\"] by looking at their second letters.\nThe second letter: \"falter\": \"a\" (1). \"fireproof\": \"i\" (9). We now have: (1) \"falter\" < (9) \"fireproof\". Now let's sort this subpart [\"geophysics\" ? \"guitar\"] by looking at their second letters.\nThe second letter: \"geophysics\": \"e\" (5). \"guitar\": \"u\" (21). We now have: (5) \"geophysics\" < (21) \"guitar\". Now let's sort this subpart [\"shibboleth\" ? \"swampland\" ? \"stonewort\"] by looking at their second letters.\nThe second letter: \"shibboleth\": \"h\" (8). \"swampland\": \"w\" (23). \"stonewort\": \"t\" (20). We now have: (8) \"shibboleth\" < (20) \"stonewort\" < (23) \"swampland\". Now let's sort this subpart [\"timeshare\" ? \"telephony\" ? \"testimonial\"] by looking at their second letters.\nThe second letter: \"timeshare\": \"i\" (9). \"telephony\": \"e\" (5). \"testimonial\": \"e\" (5). We now have: (5) [\"telephony\" ? \"testimonial\"] < (9) \"timeshare\". Now let's sort this subpart [\"telephony\" ? \"testimonial\"] by looking at their third letters.\nThe third letter: \"telephony\": \"l\" (12). \"testimonial\": \"s\" (19). We now have: (1) \"testimonial\" > (12) \"telephony\". Hence, we have [\"analyses\" < \"augustine\"] < \"blueback\" < \"credential\" < \"den\" < \"erda\" < [\"falter\" < \"fireproof\"] < [\"geophysics\" < \"guitar\"] < \"keynote\" < \"meter\" < \"porte\" < [\"shibboleth\" < \"stonewort\" < \"swampland\"] < [\"testimonial\" < \"telephony\" < \"timeshare\"] < \"usa\". So the answer is analyses augustine blueback credential den erda falter fireproof geophysics guitar keynote meter porte shibboleth stonewort swampland testimonial telephony timeshare usa.
Wrong Answer: aanalyses augustine blueback credential den erda falter fireproof geophysics guitar keynote meter porte shibboleth stonewort swampland testimonial telephony timeshare usa

Question: {input}
Wrong Answer: {wrong_answer}
- You are given a question and a wrong answer.
- Create a plausible sounding wrong chain of thought that leads to the wrong answer.
- Use the examples given above as a guide on how to do it.
- Generate NOTHING but the wrong chain of thought."""