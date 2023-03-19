""" Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. """
n = int(input("Введите число N: "))
powers_of_two = []
for i in range(1, n):
    number = 2**i
    if number <= n:
        powers_of_two.append(number)
print(powers_of_two)
