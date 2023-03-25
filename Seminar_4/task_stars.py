""" Напишите функцию , которая будет возвращать переданное в качестве параметра n число словами
Input -> 435467
Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь """

def number_to_words(n):
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
             'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ["", 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    # Функция для преобразования числа от 1 до 999
    def convert_hundreds(num):
        if num == 0:
            return ''
        elif num <= 9:
            return ones[num]
        elif num <= 19:
            return teens[num - 10]
        elif num <= 99:
            return f"{tens[num // 10 - 2]} {ones[num % 10]}"
        else:
            return hundreds[num // 100] + " " + convert_hundreds(num % 100)

    # Основная функция для преобразования числа в слова
    if n == 0:
        return "ноль"
    elif n < 0:
        return f"минус {number_to_words(abs(n))}"
    else:
        words = ''
        i = 0
        while n > 0:
            if n % 1000 != 0:
                word = convert_hundreds(n % 1000)
                if i > 0:
                    word = word + ' тысяч'
                if words != '':
                    words = word + ' ' + words
                else:
                    words = word
            n = n // 1000
            i += 1
        return words


num = int(input("Введите число для перевода в текст: "))
print(number_to_words(num))
