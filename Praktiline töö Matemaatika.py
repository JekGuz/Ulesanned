from random import *
from math import *
import random


print("Добро Пожаловать на проверку математических знаний")
print("На ваш выбор предлогается три урованя:\n1 Уровень для новичков\n2 уровень более сложный\n3 уровень для более опотных")
N = int(input("Сколько раз будем решать примеры: "))
lv = int(input("Введите уровень сложности: "))
for i in range(1,N+1,1):
    if lv == 1:
        num1 = random.randint(1, 10)  #random.randint(start, stop)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-"])   #Метод choice()возвращает случайно выбранный элемент из указанной последовательности, в мое случаии списка
    elif lv == 2:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["*", "/"])
    else:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 10)
        operation = random.choice(['**', '+', '-', '*'])

    # question =print(f"{i+1}.{num1} {operation} {num2}")
    # answer = input("Какой ответ: ")
    # if answer == correct_answer
    #     print(f"Правльный {answer}")
    # else:
    #     print(f"Ответ не верный, правильный ответ: {correct_answer}")

    if operation == "/" and num2 == 0:
        num2 = 1  # Избегаем деления на ноль
    question = f"{num1} {operation} {num2}"
    correct_answer = eval(question)
    correct_answer = round(correct_answer, 2) if operation == '/' else correct_answer

    print(f"{i}. {question}")
    answer = float(input("Какой ответ: "))
    if answer == correct_answer:
        print("Правильно!")
        correct = int(+1)   #не считает почему????????? я думала запишит == плохо, + хотя бы дает дальше идти
    else:
        print(f"Ответ не верный, правильный ответ: {correct_answer}")

hind = int((correct / N) * 100)
print("\nТест завершен!")
print(f"Правильных ответов: {correct} из {N} оценка {round(hind,2)} ")
if hind < 60:
    grade = "Оценка 2"
elif 60 >= hind < 75:
    grade = "Оценка 3"
elif 75 >= hind < 90:
    grade >= "Оценка 4"
else:
    grade = "Оценка 5"

print(f"Ваша оценка: {grade}")
print("Спасибо за участие!")

