# -*- coding: utf-8 -*-
# author: ALEX MARKOV
"""Модуль бинарного поиска заданных целочисленных значений
"""
def binary_search(list, item):
    """ Функция бинарного поиска заданного числа в заданной последовательности целых чисел от 0 до n

    >>>import binary_search
    >>>my_list = [0,1,2,3,4,5,6,7,8,9,10] # или my_list = range(n)
    >>>item = 7
    >>>binary_search([1,2,3,4,5,6,7,8,9,10], 7)

    #,где переменная my_list - любая последовательность положительных целочисленных значений, а переменная item - искомое целое положительное число
    """
    
    low = 0 
    high = len(list)-1
    score = 0
    while low <= high:
        mid = int((low + high)/2) # int(...)/2
        guess = list[mid]
        if guess == item:
            return "Число = " + str(mid), "Кол-во итераций = " + str(score)
        if guess > item:
            high = mid - 1
            score += 1
        else:
            low = mid + 1
            score += 1
    return None


if __name__ == "__main__":
    my_list = range(1000000)
    item = 54464
    #print(list(my_list)) # если у Вас есть время можете удалить коммент данной инструкции
    print (binary_search(my_list, item))
    print (binary_search(my_list, 1548))
