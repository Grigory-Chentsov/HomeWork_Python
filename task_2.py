""" Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
******Рассмотрите вариант, что он также делают журавлики в момент подсчета и известно только число уже полностью готовых
"""
S = int(input("Введите общее кол-во журавликов: "))  # вводим количество журавликов
petr = 0
kat = 0
serg = 0
while S > 0:
    for item in range(1, S+1):
        kat = item // 3 * 2  # вычисляем количество журавликов, которые сделала Катя
        petr_serg= (item - kat) // 2  # вычисляем количество журавликов, которые сделали Петя и Сережа
        petr = petr_serg
        serg = petr_serg
        made = kat + petr + serg
        print(made)  # выводим результат общий за одну итерацию
        S -= 1
print(petr, kat, serg)  # выводим результат

