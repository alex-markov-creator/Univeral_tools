# Встроенный менеджер контекста
f = open('hello.txt', 'w')
try:
    f.write('привет, мир!')
finally:
    f.close()

# Поддержка инструкции with в собственных объектах
class ManagedFile:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
with ManagedFile('hello.txt') as f:
    f.write('еще одна запись!')
    f.write('а теперь пока!')

# Несколько абстракций поверх протокола менеджера контекста
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello.txt') as f:
    f.write('запись после записи!')
    f.write('теперь точно пока!')

    
# API с менеджерами контекста
class Indenter:
    """
    Менеджер контекста для расстановки отступов
    """
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)

with Indenter() as indent:
    indent.print('привет!')
    with indent:
        indent.print('здорово')
        with indent:
            indent.print('бонжур')
    indent.print('эй')
    

    
