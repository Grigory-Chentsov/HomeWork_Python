""" Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств. """

n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

array_n = set()
array_m = set()
len_arrays = len(array_m) + len(array_n)


def fill_array():
    while len_arrays <= n + m:
        if len(array_n) < n:
            array_n.add(int(input("для заполнения массива, введите целое число: ")))
        elif len(array_m) < m:
            array_m.add(int(input("для заполнения массива, введите целое число: ")))
        else:
            return array_n, array_m


fill_array()
result = set.union(array_n, array_m)

print(result)
