
questions = []
user_ans = ""

def load_questions():
    global questions
    questions = [
        {"question": "The blue colour of the clear sky is due to", "options": ["A. Diffraction of light", "B. Dispersion of light", "C. Reflection of light", "D. Refraction of light"], "answer": "B"},
        {"question": "Fathometer is used to measure", "options": ["A. Earthquakes", "B. Rainfall", "C. Ocean depth", "D. Sound intenity"], "answer": "C"},
        {"question": "What gas is used to extinguish fires?", "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon dioxide", "D. Hydrogen"], "answer": "B"},
        {"question": "What is the largest ocean on Earth?", "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Southern Ocean", "D. Pacific Ocean"], "answer": "D"},
        {"question": "Which planet in the solar system is known as the “Red Planet”?", "options": ["A. Mars", "B. Jupiter", "C. Saturn", "D. Neptune"], "answer": "A"},
    ]

def welcome_message():
    print("Welcome to the Quiz Game! Topic: General Knowledge")
    print("Rules: Answer the multiple-choice to test your knowledge.")
    print("For each correct answer, you will earn a point.")
    print("Let's get started!\n")

def present_question(question):
    global user_ans
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_ans = input("Please select an answer (A/B/C/D): ")

def evaluate_answer(question, user_ans,score):
    answer = question["answer"]
    if user_ans.upper() == answer:
        print("Correct!")
        return score + 1
    else:
        print("Incorrect. The correct answer is: " + answer)
        return score

def display_final_results(score, total_questions):
    print(f"Your final score is: {score} out of {total_questions}")
    if score == total_questions:
        performance_message = "Excellent!" 
    else:
        performance_message = "Good effort!"
    print(performance_message)

def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again == "yes"

def start_game():
    welcome_message()
    load_questions()
    total_questions = len(questions)
    score = 0
    
    for question in questions:
        present_question(question)
        score = evaluate_answer(question, user_ans, score)
    
    display_final_results(score, len(questions))
    
    if play_again():
        start_game()
    else:
        print("Thank you for playing.")

start_game()
