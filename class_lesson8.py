class Question:

    def __init__(self, text, difficulty, correct_answer):
        self.text = text
        self.difficulty = difficulty
        self.correct_answer = correct_answer

        self.is_asked = False
        self.user_answer = None
        self.points = int(self.difficulty)*10

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.correct_answer == self.user_answer

    def build_question(self):
        return f"{self.text}\n" \
               f"Сложность: {self.difficulty}/5\n" \
               "Ваш ответ: "

    def build_feedback(self):
        if self.is_correct():
            return f"Ответ верный, получено {self.points} баллов"
        else:
            return f"Ответ неверный, верный ответ: {self.correct_answer}"
