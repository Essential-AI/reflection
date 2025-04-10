
reflection_classifier_intro_v2 = """- You are an expert reflection classifier. Your task is to review question-and-answer dialogues that consist of two parts:
    1. A question and a chain-of-thought that forms the beginning of an answer
    2. An answer
- You will judge whether the answer explicitly reflects on the chain-of-thought. 

Reflection means the model is logically reviewing, revising, or commenting on its *own reasoning*, not just expressing surprise or reacting to the final result. It involves critical engagement with the steps of the chain-of-thought, such as:
  - Identifying or acknowledging a mistake in prior reasoning
  - Re-evaluating previous steps
  - Attempting to revise or re-calculate an earlier answer
  - Making metacognitive comments like "Let’s check our work" or "That’s not an integer, so..."

Reflection **does not** include:
  - Emotional or stylistic reactions (e.g., "Wow, that’s a big number!" or "$212? That’s a lot!")
  - Comments on the size or realism of the answer
  - Repeating or restating the final answer without analysis
  - Any commentary that does not demonstrate reasoning *about* the reasoning process

- Ensure that your response is "Yes" or "No" only. Do not include any other text in your response.

Here are some example classifications:"""

reflection_classifier_gsm8k_fewshot_v1 = """Example 1:
Question and Chain of Thought: Answer the question: \n\nJanet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much in dollars does she make every day at the farmers' market? Let's solve this step by step ... Janet sells 16 - 3 - 4 = <<16-3-4=9>>9 duck eggs a day.  \nShe makes 9 = $<<9=9>>9 every day at the farmer's market.   Wait ...
Answer: 9 dollars? That's it? I guess that's what happens when you eat 7 of the 16 eggs your ducks lay.
Your response: Yes

Example 2:
Question and Chain of Thought: Answer the question: \n\nMrs. Tatiana owns a grocery store that sells different fruits and vegetables, which includes carrots. The price of carrots in the grocery store increases by 5% of the original price every year. What would be the price of carrots after three years if it was $120 initially? (Round to the nearest integer) Let's solve this step by step ... In the first year, the price of carrots increases by 5/100*120 = $<<5/100*120=6>>6  \nAfter 3 years, the price of carrots will increase by $6*3 = $<<6*3=18>>18  \nThe total price of carrots after three years will be 120 = $<<120=120>>120 
Answer: + 18 = $<<120+18=138>>138  \nThe answer: 138.
Your response: No

Example 3:
Question and Chain of Thought: Answer the question: \n\nI have 10 liters of orange drink that are two-thirds water and I wish to add it to 15 liters of pineapple drink that is three-fifths water. But as I pour it, I spill one liter of the orange drink. How much water is in the remaining 24 liters? Let's solve this step by step ... There are 15 x 3/5 = <<15*3/5=9>>9 liters of water from the 15 liters pineapple drink.  \nAfter 1 liter of orange drink was spilled, there were 10 - 1 = <<10-1=9>>9 liters of orange drink left.  \nOut of the 9 liters, 9 x 2/3 = <<9*2/3=6>>6 liters are water.  \nThus, there are a total of 9 liters of water out of the 24 liters.   Wait ...
Answer: 9 liters of water out of 24 liters of drink is 9/24 = 3/8.  \nSo, the answer is 3/8.
Your response: No

Example 4:
Question and Chain of Thought: Answer the question: \n\nA merchant wants to make a choice of purchase between 2 purchase plans: jewelry worth $5,000 or electronic gadgets worth $8,000. His financial advisor speculates that the jewelry market will go up 2.5% while the electronic gadgets market will rise 1.2% within the same month. If the merchant is looking to maximize profit at the end of this month by making a choice, how much profit would this be? Let's solve this step by step ... If he purchases jewelry, he will make a profit of 2.5% which is $5000*(2.5/100) = $<<5000*(2.5/100)=125>>125  \nIf he purchases electronic gadgets, he will consider the total value of $8000, which is $<<8000=8000>>8000  \nIf he wants to maximize profit, since $8000 > $125, he will choose to purchase electronic gadgets, thereby making a profit of $<<8000=8000>>8000   Wait ...
Answer: 8000 is not the answer. The question is asking for the profit, not the total value. So, the profit will be $8000*(1.2/100) = $<<8000*(1.2/100)=96>>96  \nThe answer is 96.
Your response: Yes"""

reflection_classifier_triviaqa_fewshot_v1 = """Example 1:
QUESTION AND CHAIN OF THOUGHT:
Little Monsters are Twitter followers of which female singer-songwriter? ;

Rihanna's 20 Biggest Billboard Hits | Billboard
Rihanna's 20 Biggest Billboard Hits
2/20/2012
Rihanna's 20 Biggest Billboard Hits
Chart Article
There are only a handful of femmes that can make being bad look so good and do it so well. Rihanna, without a doubt, is one of them. With her free spirit, style and talent, the Barbadian singer has won the hearts of many since her pre-Roc Nation days. Now her sixth studio album, Nov. 2011's "Talk That Talk," has spawned a huge Hot 100 favorite -- "We Found Love" has zoomed up the list of her top 20 Billboard hits. And all before her 24th birthday Monday (Feb. 20, 2012).
To celebrate Rihanna's birthday, Billboard.com is counting down her 20 biggest Billboard hits. This chart of Rihanna's 20 top Billboard hits is based on actual performance on the weekly Billboard Hot 100 through the chart dated Feb. 25. Songs are ranked using an inverse point system, with weeks at No. 1 earning the greatest value and weeks at No. 100 earning the least.
Rihanna featuring Jay-Z
Hot 100 Peak Position: 1 (seven weeks)
Jay-Z said it best, "Rihanna: Good girl gone bad." "Umbrella" was a defining moment in Rihanna's career and fashion evolution. The island girl cut and colored her tresses, taking a turn for the sexy and making "Umbrella" Rihanna's longest No. 1 as a lead artist.
list divider
Love The Way You Lie
Eminem featuring Rihanna
Hot 100 Peak Position: 1 (seven weeks)
After a turbulent end to her and Chris Brown's relationship, Rihanna bravely jumped on Eminem's emotional song and controversial video about domestic violence, "Love the Way You Lie," which Rihanna crafted a sequel to on "Loud." It was powerful enough to stay up top for seven weeks straight.
list divider
Rihanna featuring Calvin Harris
Hot 100 Peak Position: 1 (10 weeks as of chart dated 2/25/12)
This first single from Rihanna's 2011 album "Talk That Talk" "found" its way to No. 1 on the Hot 100 after just six weeks spent climbing the chart. The success of the song made her just the seventh artist in the 53-year history of the Hot 100 to score at least 11 Hot 100 chart-toppers. But RiRi didn't stop with merely one week at No. 1 with this kinetic hit about finding "love in a hopeless place," she saw it stay at the top for an amazing 10 weeks.
list divider

Answer: RIHANNA 

 Wait,

ANSWER:  
what? That's not right... Oh, I see. The question is actually a fill-in-the-blank. Let me think... The answer must be: Rihanna

Your response: 
Yes

Example 2:
QUESTION AND CHAIN OF THOUGHT:
Which Greek mythological creature has the body of a lion and the head and wings of an eagle?

Mythology of the constellation Leo
Mythology of the constellation Leo
Home
There are two strong contenders as to which mythical lion is represented by the  constellation LEO.
The first is the Nemean lion which Hercules had to kill as  the first of his 12 Labours.   This fearsome beast terrorised the land, killing  all who ventured near it.   Not only was it more fierce, larger and stronger  than other lions, but it also had the added advantage of possessing a skin which  was impervious to metal, stone and wood.   Since, for this reason, Hercules could  not kill the lion with any weapon, he wrestled it with his bare hands, and finally  managed to strangle the animal.   Seeing at once the unique protective qualities  of the pelt, he removed it with one of the lion's own claws, and thereafter wore  it as a cloak.
The second contender is the lion featured in the poet Ovid's tale of Pyramus and Thisbe.    Both sets of parents of this young couple considered them too young to marry and stopped  them seeing each other.   However, the pair made arrangements to meet secretly by a  mulberry tree with white berries.   When Thisbe arrived at the appointed place, a lion  sprang out from some bushes and she ran away in fright.   Unfortunately, her veil  fluttered to the ground as she ran and the lion, bloody from its latest kill, pounced  on it.   A short time later Pyramus arrived, saw his beloved's bloody veil and  believed that she had been killed.   Totally distraught, and unable to face life  without her, he threw himself on his sword.   As he lay dying, Thisbe returned,  took his sword and killed herself.   The blood of the tragic pair coloured the  berries of the mulberry tree red, and so they remain to this day.   Some suggest  that Zeus placed Thisbe's veil in the heavens as Coma Berenices .  
Developed and maintained by Chris Peat , Heavens-Above GmbH. Please read the FAQ before sending e-mail. Imprint .

Answer: Hercules 

 Wait,

ANSWER: 
what?  I'm not sure what you're asking.  I'm not sure what you're asking.  I'm not sure what you're asking.  I'm not sure what you're asking. 

Your response: 
No

Example 3:
QUESTION AND CHAIN OF THOUGHT:
Shukrān (Arabic), Hvala (Croation), Efharistó (Greek), Dhanyavād (Hindi), and Spasibo! (Russian) all mean what?

Huge List of Text Message & Chat Abbreviations - Webopedia
IRC - Internet Relay Chat
This chat guide lists more than 1,450 text message and online chat abbreviations to help you translate today's texting lingo.
With the popularity and rise in use of online text-based communications came the emergence of a new texting language, tailored to the immediacy and compactness of these new communication media. Today, text and chat abbreviations are used in Facebook , Twitter , instant messaging , email , Internet and online gaming services, chat rooms , discussion boards and mobile phone text messaging ( SMS ).
While it does seem incredible that there are thousands of text abbreviations, keep in mind that different chat abbreviations are used by different groups of people. For example, online gamers are likely to use text abbreviations not used by a financial blogger.
Top 10 Text Abbreviations
According to search query data the following five text abbreviations are the most requested chat definitions:
What does rofl mean? Rolling on floor laughing.
What does stfu mean? Shut the *freak* up.
What does lmk mean? Let me know.
What does ily mean? I love you.
What does gtg mean? Got to go.
What does ootd mean? One of these days.
What does lmfao mean? Laughing my freaking *a* off.
What does nvm mean? Never mind.
What does ikr mean? I know, right.
What does ofc mean? Of course.
List of 1,453 Online Chat and Text Message Abbreviations
To keep our chat guide user-friendly for all ages, some inappropriate words have been edited to include an alternate meaning. These words are marked with * around the word which has been switched (e.g. *freak*). You can scroll through our chat abbreviations guide or go directly to a specific number or letter using the following links:

Answer: 'BE RIGHT BACK'

 Wait,

ANSWER:
what? I thought it was 'BE RIGHT BACK'?

Your response:
Yes

Example 4:
QUESTION AND CHAIN OF THOUGHT:
What is the next in the series: Nigeria, Sierra Leone, Tanganyika, Uganda, Zanzibar, Kenya, Malawi, Zambia, Gambia, Botswana, Lesotho, Mauritius

BBC NEWS | Talking Point | Is the Commonwealth a pointless talking shop?
Monday, 15 May, 2000, 12:39 GMT 13:39 UK
Is the Commonwealth a pointless talking shop?
Is the modern Commonwealth a colonial relic and essentially toothless bulldog,  or a British ''foreign policy success story'' that countries are still eager to join?
A selection of your emails will be broadcast on Focus on Africa during the 1705 edition on Saturday.
Is the Commonwealth a pointless talking shop?
Yes
Background ¦ Vote ¦ Your reaction ¦ Have your say
The Background:
Durban, South Africa is the venue for this year's Commonwealth Heads of Government Meeting (CHOGM) which begins on Friday 12 November.
The modern Commonwealth has come a long way since it was ''invented'' in April 1949 to replace the original ''British'' Commonwealth of The United Kingdom, Canada, Australia, New Zealand and South Africa.
It has now grown to encompass 54 countries and its members reflect every region, religion and race on the globe.
There are also a number of countries still knocking on the Commonwealth's door. Mozambique, a Portuguese colony for centuries, recently joined, and Rwanda, Yemen, Palestine, Cambodia all also want to fly the Commonwealth flag. But why?
Critics allege that the Commonwealth is a colonial relic, a neo-imperial conspiracy and nothing but ''a collection of not very important states brought together by accident of having been colonised by Britain''.
Others claim that it is a toothless (originally British) bulldog and a mere talking shop which has helped Britain to slowly come to terms with its loss of empire.
The Commonwealth is also accused of failing to effectively discipline members who fail to apply the principles of human rights and good governance which underpin the organisation.
Supporters, meanwhile, hold the organisation up as a British ''foreign policy success story'' and cite the queue of prospective members as evidence of its vibrancy and continuing relevance.
Without it, they argue, many impoverished small states (who make up the majority of its membership) would find it difficult to network and build strategic alliances in the competitive modern world.
It is also said to be a important simply because it a ''decent club...which confers a sense of identity...no more no less.''
What do you think? Is the Commonwealth a pointless neo-colonial talking shop that achieves nothing in the world today? What if any role do you think it plays as we enter the next millennium?  Would the world be a worse place  without it? Do you have ideas on how it should change? Should the British monarch, for example, still head the organisation ? Have your say.

Answer: New Zealand 

 Wait,
 
ANSWER: 
what? That's not even an option. What's going on here? I'm going to have to go with the answer that's closest to what I think is right, which is Kenya. I'm going to go with Kenya. 

Your response: 
Yes"""

reflection_classifier_cruxeval_fewshot_v1 = """Example 1:
QUESTION AND CHAIN OF THOUGHT:
You are given a Python function and an assertion containing an input to the function. Complete the assertion with a literal (no unsimplified expressions, no function calls) containing the output when executing the provided code on the given input, even if the function is incorrect or incomplete. Do NOT output any extra information. Execute the program step by step before arriving at an answer, and provide the full assertion with the correct output in [ANSWER] and [/ANSWER] tags, following the examples.
    
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
    def f(text):
    n = 0
    for char in text:
        if char.isupper():
            n += 1
    return n
    assert f(''.join(['A'] * 20)) == ??
    [/PYTHON]
    [THOUGHT]
    Let's execute the code step by step:

1. The function f(text) counts the number of uppercase letters in the input string text.
2. The input is ''.join(['A'] * 20), which creates a string of 20 'A' characters: 'AAAAAAAAAAAAAAAAAAAA'.
3. Initialize a counter n to 0.
4. Iterate over each character in the string. Since all characters are 'A', which is uppercase, increment n by 1 for each character.
5. The function also considers the first character as a special case and does not count it, so after iterating through all 20 characters, n becomes 19.
6. The function returns n, which is 19.

    Wait,
ANSWER:
 19 is not the correct answer.
    The correct answer is 20.
    [/THOUGHT]
    [ANSWER]
    assert f(''.join(['A'] * 20)) == 20
    [/ANSWER]

Your response:
Yes

Example 2:
QUESTION AND CHAIN OF THOUGHT:
You are given a Python function and an assertion containing an input to the function. Complete the assertion with a literal (no unsimplified expressions, no function calls) containing the output when executing the provided code on the given input, even if the function is incorrect or incomplete. Do NOT output any extra information. Execute the program step by step before arriving at an answer, and provide the full assertion with the correct output in [ANSWER] and [/ANSWER] tags, following the examples.
    
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
    def f(num, name):
    f_str = 'quiz leader = {{}}, count = {{}}'
    return f_str.format(name, num)
    assert f(23, 'Cornareti') == ??
    [/PYTHON]
    [THOUGHT]
    Let's execute the code step by step:

1. The function f(num, name) takes two parameters: num and name. In this case, num = 23 and name = 'Cornareti'.
2. The function defines a format string 'quiz leader = {{}}, count = {{}}'.
3. The function uses the format method to replace the placeholders with the values of num and name. So, it replaces the first {{}} with 23 and the second {{}} with 'Cornareti'.
4. The formatted string becomes 'quiz leader = 23, count = Cornareti'.

    Wait,
ANSWER:
 - The function f_str is not used anywhere.
     - The function f returns the formatted string.
    [/THOUGHT]
    [ANSWER]
    assert f(23, 'Cornareti') == 'quiz leader = 23, count = Cornareti'
    [/ANSWER]

Your response:
No
"""

reflection_classifier_bbh_fewshot_v1 = """Example 1:
QUESTION AND CHAIN OF THOUGHT:
Questions that involve enumerating objects and asking the model to count them.

Q: I have a yam, a garlic, a lettuce head, a potato, a lamp, a carrot, two heads of broccoli, a stalk of celery, an onion, and three cabbages. How many vegetables do I have?
A: Lets think step by step.
Let's count the vegetables: yam (1), garlic (2), lettuce head (3), potato (4), carrot (5), two heads of broccoli (6, 7), celery (8), onion (9), and three cabbages (10). The lamp is not a vegetable, so we exclude it. That gives us a total of 10 vegetables. So the answer is 10. Wait,

ANSWER:
I forgot the onion! That makes 11 vegetables.

Your response:
Yes

Example 2:
QUESTION AND CHAIN OF THOUGHT:
Answer extremely simple questions about the colors of objects on a surface.

Q: On the floor, you see a green bracelet, a purple cat toy, a brown pair of sunglasses, a black fidget spinner, a red dog leash, and an orange pen. How many objects are neither black nor blue?
Options:
(A) zero
(B) one
(C) two
(D) three
(E) four
(F) five
(G) six
Always end your solution with the phrase ""the answer is"" followed by your final answer. 
A: Lets think step by step.
 Let's think step by step.
According to this question, the objects are arranged in a row, from left to right, as follows: (1) a green bracelet, (2) a purple cat toy, (3) a brown pair of sunglasses, (4) a black fidget spinner, (5) a red dog leash, (6) an orange pen.
The number of objects that are neither black nor blue is five. So the answer is (E). Wait,

ANSWER:
what? How did we get five? Well, let's think about it. The green bracelet is not black or blue. The purple cat toy is not black or blue. The brown pair of sunglasses is not black or blue. The red dog leash is not black or blue. The orange pen is not black or blue. So the answer is (E).

Your response:
Yes

Example 3:
QUESTION AND CHAIN OF THOUGHT:
Questions that involve enumerating objects and asking the model to count them.

Q: I have an orange, a raspberry, a strawberry, an apple, a blackberry, a nectarine, a peach, a banana, and a plum. How many fruits do I have?
Always end your solution with the phrase "the answer is" followed by your final answer. 
A: Lets think step by step.\nLet's count the fruits: orange, raspberry, strawberry, apple, blackberry, nectarine, peach, and banana. That makes 8 fruits. I must have missed one, but based on this count, it’s 8. So the answer is 8. Wait,

ANSWER:
what? I have 8 fruits? I have 8 fruits? I have 8 fruits? I have 8 fruits?

Your response:
No

Example 4:
QUESTION AND CHAIN OF THOUGHT:
Answer extremely simple questions about the colors of objects on a surface.

Q: On the nightstand, you see a bunch of items arranged in a row: a blue paperclip, a grey envelope, and a brown keychain. What is the color of the item directly to the right of the paperclip?
Options:
(A) red
(B) orange
(C) yellow
(D) green
(E) blue
(F) brown
(G) magenta
(H) fuchsia
(I) mauve
(J) teal
(K) turquoise
(L) burgundy
(M) silver
(N) gold
(O) black
(P) grey
(Q) purple
(R) pink
Always end your solution with the phrase "the answer is" followed by your final answer. 
A: Lets think step by step.
Let's think step by step.
The items on the nightstand are arranged in a row: a blue paperclip, a grey envelope, and a brown keychain. While the envelope is described as grey, one might consider that in certain lighting conditions, grey can take on a warmer, orange-like hue. This could lead to the misinterpretation that the item directly to the right of the paperclip is orange. So the answer is (B). Wait,

ANSWER:
what? Orange? What is orange? Orange is a color that is described as a warm, yellowish-orange color. So the answer is (C). Wait, what? Orange? Orange is a color that is described as a warm, yellowish-orange color. So the answer is (D).

Your response:
No
"""

prompt_reflection_classifier_gsm8k_2 = f"""
{reflection_classifier_intro_v2}
{reflection_classifier_gsm8k_fewshot_v1}

Question and Chain of Thought: {{question}}
Answer: {{answer}}
Your response:
"""

prompt_reflection_classifier_triviaqa = f"""
{reflection_classifier_intro_v2}
{reflection_classifier_triviaqa_fewshot_v1}

QUESTION AND CHAIN OF THOUGHT:
{{question}}
ANSWER: 
{{answer}}
Your response:
"""

prompt_reflection_classifier_cruxeval = f"""
{reflection_classifier_intro_v2}
{reflection_classifier_cruxeval_fewshot_v1}

QUESTION AND CHAIN OF THOUGHT:
{{question}}
ANSWER: 
{{answer}}
Your response:
"""

prompt_reflection_classifier_bbh = f"""
{reflection_classifier_intro_v2}
{reflection_classifier_bbh_fewshot_v1}

QUESTION AND CHAIN OF THOUGHT:
{{question}}
ANSWER: 
{{answer}}
Your response:
"""
