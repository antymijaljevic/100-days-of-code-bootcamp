from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# new_q = Question("What is there?", "True")

# print(new_q.text)
# print(new_q.answer)

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()