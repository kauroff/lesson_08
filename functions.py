import json
import random


def load_question(filename):
    with open(filename, encoding='utf-8') as file:
        list_of_questions = json.load(file)
        random.shuffle(list_of_questions)

    return list_of_questions


def print_statistics(questions, total, points):
    return f"Вот и все!\n" \
           f"Отвечено на {total} из {len(questions)}\n" \
           f"Набрано баллов: {points}."