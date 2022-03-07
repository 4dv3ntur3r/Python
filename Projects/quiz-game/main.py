from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)  # if used += instead of append you will get an error

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

# if needed use this link to generate new questions https://opentdb.com/
