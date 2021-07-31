class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        position = self.question_number
        current_question = self.question_list[position]
        question_text = current_question.text

        input(f"Q.{position}: {question_text} (True/False)")
