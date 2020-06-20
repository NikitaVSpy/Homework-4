# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого
# списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию
# random);

import random

name = ['Форрест', 'Джулс', 'Джон', 'Джеймс', 'Вито', 'Элен', 'Джек', 'Джеффри', 'Индиана',
        'Хан', 'Тайлер', 'Рик', 'Арагорн', 'Тони', 'Марти', 'Майкл', 'Феррис', 'Уолтер', 'Рокки']


def func(number, *args):
    name_list = []
    for i in range(0, number, 1):
        name_list.append(random.choice(args))
    return name_list


random_list = func(100, *name)
print(random_list)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
from collections import Counter


def most_encountered(list_name):
    occurence_count = Counter(list_name)
    return occurence_count.most_common(1)[0][0]


print('Наиболее встречающееся имя в списке:', most_encountered(random_list))


# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def rare_letter(list_letter):
    first_letter = list(map(lambda x: x[0], list_letter))
    occurence_letter = Counter(first_letter)
    return occurence_letter.most_common()[-1:][0]

print('Наименее встречающаяся первая буква имени в списке:', rare_letter(random_list))
