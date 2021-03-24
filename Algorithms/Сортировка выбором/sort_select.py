# -*- coding: utf-8 -*-
# author: Alex Markov
"""Сортировка выбором - медленно
"""
def find_Smallest(arr):# запись "имени" функции (что она есть)
    smallest = arr[0] # первое значение
    smallest_index = 0 # нулевой индекс
    for i in range(1, len(arr)): # для i в (1,2,3,4)
        if arr[i] < smallest: # проверка 
            smallest = arr[i] # присваивание 
            smallest_index = i # присваивание
    return smallest_index # возврат на добавление в пустой список

def selectionSort(arr): # # запись "имени" функции (что она есть)
    newArr = []
    for i in range(len(arr)): # для i в (0,1,2,3,4)
        smallest = find_Smallest(arr) # возврат к 1-ой функции
        newArr.append(arr.pop(smallest)) # добавление в пустой список
    return newArr

print (selectionSort([5,3,6,2,10])) # начало и запуск 2-ой функции