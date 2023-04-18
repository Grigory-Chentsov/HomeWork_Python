""" | Задание 44 |
        | --- |
| В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его
в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head() | """

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

unique_values = list(set(data['whoAmI']))
one_hot = pd.DataFrame(columns=unique_values)

for value in unique_values:
    one_hot[value] = (data['whoAmI'] == value).astype(int)

data = pd.concat([data, one_hot], axis=1)
print(data.head())
