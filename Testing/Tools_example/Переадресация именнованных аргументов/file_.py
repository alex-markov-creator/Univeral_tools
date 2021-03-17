#-*- coding: utf-8 -*-
"""
*py - name file
"""
def bar(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)

def foo (x, *args, **kwargs):
    kwargs['имя'] = 'Алиса'
    new_args = args + ('дополнительный', )
    bar (x, *new_args, **kwargs)

foo(1, 'text', key1 = '02')



