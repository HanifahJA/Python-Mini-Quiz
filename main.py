# greet user
def greet_by_name(p_name):
    print(f"Welcome {p_name}!")
name = input("Enter your name: ")
greet_by_name(name)

# quiz questions and answers
class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is the capital of France?\n(a) Berlin\n(b) Madrid\n(c) Paris\n(d) Rome\nAnswer: ",
    "How many states are there in the US?\n(a) 24\n(b) 63\n(c) 51\n(d) 50\nAnswer: ",
    "How many bones are there in the adult human body?\n(a) 186\n(b) 206\n(c) 226\n(d) 246\nAnswer: ",
    "What parent company owns both Instagram and Whatsapp?\n(a) Google\n(b) Apple\n(c) Amazon\n(d) Meta\nAnswer: ",
    "The Heimlich manoeuvre is used to help someone who is:\n(a) Choking\n(b) Having a seizure\n(c) Feeling faint\n(d) In cardiac arrest\nAnswer: ",
    "What is the main function of red blood cells?\n(a) Carrying oxygen\n(b) Fighting infections\n(c) Clotting blood\n(d) Regulating body temperature\nAnswer: ",
    "What is the title of the first Harry Potter book in the UK?\n(a) Harry Potter and the Chamber of Secrets\n(b) Harry Potter and the Philosopher's Stone\n(c) Harry Potter and the Sorcerer’s Stone\n(d) Harry Potter and the Prisoner of Azkaban\nAnswer: ",
    "What is the capital city of Australia?\n(a) Sydney\n(b) Melbourne\n(c) Canberra\n(d) Brisbane\nAnswer: ",
    "Which country is the largest by land area?\n(a) Canada\n(b) China\n(c) United States\n(d) Russia\nAnswer: ",
    "Which human organ can regenerate itself if a part of it is removed?\n(a) Heart\n(b) Brain\n(c) Liver\n(d) Pancreas\nAnswer: "
]

questions = [
    question(question_prompts[0], "c"),
    question(question_prompts[1], "d"),
    question(question_prompts[2], "b"),
    question(question_prompts[3], "d"),
    question(question_prompts[4], "a"),
    question(question_prompts[5], "a"),
    question(question_prompts[6], "b"),
    question(question_prompts[7], "c"),
    question(question_prompts[8], "d"),
    question(question_prompts[9], "c")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        # validate user input
        while answer not in ["a","b","c","d"]:  
                print(f"'{answer}' is not a valid answer.\nPlease enter 'a', 'b', 'c' or 'd'")
                answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("Correct!😄")
        else:
             print(f"Incorrect☹️. The correct answer is {question.answer}.")
    print(f"You got {score}/{len(questions)} correct.")
 
          
    #     if answer == question.answer:
    #         score += 1
    # print(f"You got {score}/{len(questions)} correct.")
# def run_quiz(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         while True:
#             if answer != "a" and answer != "b" and answer != "c" and answer != "d":
#                 print(f"'{answer}' is not a valid answer.\nPlease enter 'a', 'b', 'c' or 'd'")
#             # break
            
#         if answer == question.answer:
#             score += 1
#     print(f"You got {score}/{len(questions)} correct.")


run_quiz(questions)

# thank user
def thank_user(name):
    print(f"Thank you {name} for taking the quiz.")

thank_user(name)