""" Задача 18:
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X
*Пример:*
5
1 2 3 4 5
6         -> 5 """

N = int(input("Введите сколько чисел в массиве: "))
x = int(input("Введите ваше число: "))

array = [i for i in range(1, N + 1)]


def search_neighbor(array, x):
    max_neighdor = 0
    min_neighdor = 0
    for i in array:
        if i - 1 == x:
            max_neighdor = i
        elif i + 1 == x:
            min_neighdor = i
    if x > len(array):
        return print(f"Ближайшее по величине число в массиве - {min_neighdor}")
    else:
        return print(f"Ближайшее больше число {max_neighdor},\n Ближайшее меньшее число {min_neighdor}")


search_neighbor(array, x)

