from question_model import Question
from data import question_data, trivia_data
from quiz_brain import Quiz
from art import logo

question_bank = []
trivia_bank = []

for q in question_data:
    question_bank.append(Question(q["text"],q["answer"]))

for q in trivia_data:
    trivia_bank.append(Question(q["question"], q["correct_answer"]))

quiz = Quiz(trivia_bank)

print(logo)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")