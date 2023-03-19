"""
*** (1)У вас есть массив чисел, составьте из них максимальное число. Например:
[61, 228, 9] -> 961228 """
import random

numbers = []
while len(numbers) < 3:
    number = random.randint(1, 1000)
    numbers.append(number)
print(numbers)


def MoreNumber(numbers):
    string = ""
    while len(numbers) != 0:
        max = 0
        index = 0
        index_max = 0
        for i in numbers:
            if i > max:
                max = i
                index_max = index
            index += 1
        string += str(max)
        numbers.pop(index_max)
    return string


print(MoreNumber(numbers))





