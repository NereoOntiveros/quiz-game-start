from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    question = Question(dictionary['text'], dictionary['answer'])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

quiz_brain.next_question()
