#-*- coding=utf-8 -*-
"""
evclid.py - Алгоритм Евклида
Даны два целых положительных числа m и n.
Требуется найти их наибольший общий делитель,
т.е. наибольшее целое положительное число,
которое нацело делит оба числа m и n.
"""
import unittest
import pytest

def gcd_recursion(m: int,n: int)->int:
    """
    АЛГОРИТМ ЕВКЛИДА:
    1 Разделим m на n, и пусть остаток от деления будет равен r
    (где 0<=r<n).
    2 Если r = 0, то выполнение алгоритма прекращается; n - искомое значение.
    3 Присвоить m <-- n, n <-- r и вернуться к шагу 1.
    """
    m_int = isinstance(m, int)
    n_int = isinstance(n, int)
    if not(m_int or n_int):
        raise ValueError("Input arguments are not integers")
    elif (m_null == 0) or (n_null == 0) :
        raise ValueError("One or more input arguments equals zero")
    else:
        return (abs(m) if n==0 else gcd_recursion(abs(n), m%n))

def gcd_while(m: int,n: int)->int:
    """
    АЛГОРИТМ ЕВКЛИДА:
    1 Разделите m на n и пусть остатком будет m.
    2 Если m == 0, то работа алгоритма завершается и ответом будет n.
    3 Разделите n на m, и пусть остатком будет n.
    4 Если n=0, то работа алгоритма завершается и ответом будет m; в противном случае вернуться к первому шагу.
    """
    m_int = isinstance(m, int)
    n_int = isinstance(n, int)
    if not(m_int or n_int):
        raise ValueError("Input arguments are not integers")
    if (m == 0) or (n == 0) :
        raise ValueError("One or more input arguments equals zero")
    while n != 0:
        m, n = n, abs(m) % abs(n)
    return m

class TestGcd(unittest.TestCase):
        """[summary]
        Test for the file evclid.py

        Arguments:
            unittest {[type]} -- [description]
        """
        def test_gcd(self):
            self.assertEqual(4, gcd_while(8, 12))
            self.assertEqual(1, gcd_while(13, 17))
            self.assertEqual(57, gcd_recursion(2166, 6099))
            self.assertEqual(1, gcd_recursion(13, 17))

        def test_gcd_non_integer_input(self):
            with pytest.raises(ValueError, match=r"Input arguments are not integers"):
                gcd_while(1.0, 5)
                gcd_while(5, 6.7)
                gcd_while(33.8649, 6.12312312)
                gcd_recursion(1.0, 5)
                gcd_recursion(5, 6.7)
                gcd_recursion(33.8649, 6.12312312)

        def test_gcd_zero_input(self):
            with pytest.raises(ValueError, match=r"One or more input arguments equals zero"):
                gcd_while(0, 12)
                gcd_while(12, 0)
                gcd_while(0, 0)

        def test_gcd_negative_input(self):
            self.assertEqual(1, gcd_while(-13, -17))
            self.assertEqual(4, gcd_while(-8, 12))
            self.assertEqual(8, gcd_while(24, -16))
            self.assertEqual(1, gcd_recursion(-13, -17))
            self.assertEqual(4, gcd_recursion(-8, 12))
            self.assertEqual(8, gcd_recursion(24, -16))

if __name__ == '__main__':
    unittest.main()

