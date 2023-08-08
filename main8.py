from class_lesson8 import Question
from functions import load_question, print_statistics

print("Игра начинается!")
print()
questions = load_question("questions.json")
total = 0
points = 0
for question in questions:
    text = question['q']
    difficulty = question['d']
    correct_answer = question['a']
    question = Question(text, difficulty, correct_answer)
    user_answer = input(question.build_question())
    if question.is_correct():
        total += 1
        points += question.get_points()
    print(question.build_feedback())
    print()

print(print_statistics(questions, total, points))