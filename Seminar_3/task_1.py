""" Задача 16:
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X
*Пример:*
5
1 2 3 4 5
3         -> 1 """
import random

n = int(input("Введите кол-во чисел в массиве: "))
x = int(input("Введите какое число нужно найти в массиве: "))

# def fill_array(n):
#     array = []
#     for i in range(n):
#         array.append(random.randint(1, 10))
#     return array


array = [random.randint(1, 10) for i in range(n)]
print(array)
find_score = array.count(x)
print(f"{x} встречается {find_score} раз.")
