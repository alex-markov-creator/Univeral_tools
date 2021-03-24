#-*- coding=utf-8 -*-
"""
timsort_vs_quicksort.py - сравнение времени выполнения
аплгоритмов timsort функции sorted() из стандартной библиотеки
Python c алгоритмом выполнения быстрой сортировки на примере
сортировки списка Python со случайными значениями произвольных
чисел.
"""
import unittest
import pytest
import math
import random
import time

def quicksort(nums:list)->list:
    if not isinstance(nums, list):
        raise ValueError("Input arguments are not list")
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)

def quicksort_easy(A:list)->list:
    if not isinstance(A, list):
        raise ValueError("Input arguments are not list")
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return quicksort_easy(L) + M + quicksort_easy(R)

class TestSort(unittest.TestCase):
        """[summary]
        Test for the file evclid.py

        Arguments:
            unittest {[type]} -- [description]
        """
        def test_quicksort(self):
            self.assertEqual([1,2,3,4], quicksort([2,3,1,4]))
            self.assertEqual([1,2,3,4,5,6], quicksort([2,3,1,4,6,5]))
            self.assertEqual([1,2,3,4], quicksort_easy([2,3,1,4]))
            self.assertEqual([1,2,3,4,5,6], quicksort_easy([2,3,1,4,6,5]))

        def test_sort_non_lists_input(self):
            with pytest.raises(ValueError, match=r"Input arguments are not list"):
                quicksort('not list')
                quicksort(1)
                quicksort(a)
                quicksort_easy('not list')
                quicksort_easy(1)
                quicksort_easy(a)

        def test_values(self):
            for N in [600000, 700000, 800000, 900000]:

                start = time.perf_counter()
                lst = [i for i in range(1,N)]
                random.shuffle(lst)
                stop = time.perf_counter()
                print(f'Подготовка исходных данных = {stop-start}')

                start = time.perf_counter()
                quicksort(lst)
                print(f'Для N = {N}')
                stop = time.perf_counter()
                print(f'Время быстрой сортировки в функциональном стиле = {stop-start}')

                start = time.perf_counter()
                quicksort_easy(lst)
                stop = time.perf_counter()
                print(f'Время быстрой сортировки в императивно-декларативном стиле = {stop-start}')

                start = time.perf_counter()
                sorted(lst)
                stop = time.perf_counter()
                print(f'Время сортировки timsort = {stop-start}\n')

if __name__ == '__main__':
    unittest.main()

