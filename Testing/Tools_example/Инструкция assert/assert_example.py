#-*- coding: utf-8 -*-
"""
*py - name file
python -O *.py - assert - нулевая операция
"""
def func(x,y):
    assert 0 < x
    return x ** y


a = func(2,4)
print(a)

lst = range(-10, 10)# первый аргумент обязательно положительный!!!
# Возбуждает исключение AssertionError!!!
for i in lst:
    b = func(i, 5)
    print(b)

counter = 10

assert (2+2 == 5, "test") # Утверждение всегда верно
assert 2 + 2 == 5, "test"
