from question_model import Question
from data import question_data
from quiz_brain_2 import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

if not quiz.still_has_questions():
    print(f"You've completed the quiz!")
    print(f"Your final score was: {quiz.score}/{len(question_bank)}")


# print(question_bank[0].text)
