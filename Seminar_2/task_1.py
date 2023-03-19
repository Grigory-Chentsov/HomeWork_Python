""" Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть """
import random

while True:
    try:
        n = int(input("Введите кол-во монет: "))
        sides = ["🦅", "💲"]
        coins_list = [random.choice(sides) for i in range(n)]
        print(coins_list)
        count_eagle = 0
        count_tails = 0
        if n == 1:
            print("Введите кол-во монет больше одного.")
        else:
            for i in coins_list:
                if i == "🦅":
                    count_eagle += 1
                elif i == "💲":
                    count_tails += 1

            if count_eagle > count_tails:
                print(f"Минимальное число монет {count_tails}. Все монеты будут лежать орлом вверх.")
                break
            elif count_eagle == count_tails:
                print(f"Выпало одинаковое кол-во монет орлом и решкой, нужно перевернуть минимум {count_tails}.")
                break
            else:
                print(f"Минимальное число монет {count_eagle}, и все монеты будут лежать решкой.")
                break
    except ValueError:
        print("Введите число монет цифрами.")
