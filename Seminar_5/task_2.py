""" Задача 28:
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4 """


def summa(a, b):
    if b > 0:
        a = summa(a + 1, b - 1)
    return a


print(summa(2, 2))