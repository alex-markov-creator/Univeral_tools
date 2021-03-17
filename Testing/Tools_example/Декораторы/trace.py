#-*- coding: utf-8 -*-
"""
*py - name file
"""
def trace(func):
    """
    Регистрирует аргументы функции и итоговые рузультаты
    """
    def wrapper(*args, **kwargs):
        print(f'Трассировка: вызвана {func.__name__}() '
            f'с {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'Трассировка: {func.__name__}() '
            f'вернула {original_result!r}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

say('Джейн', 'Привет, Мир')
say('Джейн', 'Привет, Мир')
