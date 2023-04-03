""" Задача 32:
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше
заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Диапазон от 6 до 12
Вывод: [1, 9, 13, 14, 19] """

# def find_indexes(lst, x, y):
#     indexes = []
#     for i in range(len(lst)):
#         if x < lst[i] < y:
#             indexes.append(i)
#     return indexes


lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
x, y = map(int, input("Введите диапазон: ").split())
result = [i for i in range(len(lst)) if x < lst[i] < y]
# result = find_indexes(lst, x, y)
print(result)
