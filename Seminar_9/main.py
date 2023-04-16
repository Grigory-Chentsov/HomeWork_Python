""" Задача 40:
Работать с файлом california_housing_train.csv, который находится в папке sample_data.
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

Задача 42:
Узнать какая максимальная households в зоне минимального значения population
"""
import pandas as pd

data = pd.read_csv('california_housing_train.csv')

average_house_price = round(data[data['population'] < 500]['median_house_value'].mean(), 2)
max_households = data[data['population'] == data['population'].min()]['households'].max()

print(f"Средняя стоимость дома, где кол-во людей от 0 до 500 - {average_house_price}\n"
      f"Максимальная households в зоне минимального значения population - {max_households}")
