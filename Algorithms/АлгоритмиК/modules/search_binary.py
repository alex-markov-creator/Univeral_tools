# -*- coding: utf-8 -*-
# author: alex markov - agb2019@list.ru
# license: GNU General Public License
"""Модуль бинарного поиска заданных целочисленных значений
"""


def binary_search(my_numbers, numeric):
    """Функция бинарного поиска заданного числа в заданной последовательности целых чисел от 0 до n-1
    # >>>import search_binary as sb
    # >>>n = 1000
    # >>>my_numbers = range(n) # или my_numbers = [0,1,2,3,4,5,6,7,8,9,10...n-1]
    # >>>numeric = 77
    # >>>sb.binary_search(my_numbers, numeric)
    ('Число = 77', 'Кол-во итераций = 9') ,где переменная my_numbers - любая последовательность положительных целочисленных
    значений, а переменная numeric - искомое целое положительное число
    """

    low = 0
    high = len(my_numbers) - 1
    score = 0
    while low <= high:
        mid = int((low + high) / 2)  # или int(...)//2 для вещественных чисел
        guess = my_numbers[mid]
        if guess == numeric:
            return "Загаданное число = " + str(mid), "Кол-во итераций = " + str(score)
        if guess > numeric:
            high = mid - 1
            score += 1
        else:
            low = mid + 1
            score += 1
    return None


# тестирование
if __name__ == "__main__":
    print(binary_search.__doc__)
    my_values = range(999999999)
    numeric = 999999998
    # print(list(my_numbers)) # если у Вас есть время можете удалить коммент данной инструкции
    print(binary_search(my_values, numeric))
    input()
