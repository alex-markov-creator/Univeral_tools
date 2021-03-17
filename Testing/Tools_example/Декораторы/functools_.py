import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """Вернуть дружеское приветствие."""
    return 'Привет!'

print(greet.__name__)
print(greet.__doc__)
