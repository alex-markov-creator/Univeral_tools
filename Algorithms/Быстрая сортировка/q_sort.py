# -*- coding: utf-8 -*-
""" Алгоритм быстрой сортировки
"""
def quicksort(array):
    if len(array) < 2:
        return array # базовый случай
    else:
        pivot = array[0] # рекурсивный случай
        less = [i for i in array[1:] if i <= pivot] # элементы меньше опорного
        greater = [i for i in array[1:] if i > pivot] # элементы больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([10, 5, 2, 3, 7, 8])) # вывод на экран
