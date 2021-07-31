from question_model import Question
from data import question_data

question_bank = []

for dictionary in question_data:
    question = Question(dictionary['text'], dictionary['answer'])
    question_bank.append(question)
