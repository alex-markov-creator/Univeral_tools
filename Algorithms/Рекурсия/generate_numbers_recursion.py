# генерация всех перестановок (комбинаторика)
def generate_numbers(N:int, M:int, prefix = None):
    """Генерирует все числа ( с лидирующими незначащими нулями)
    в N-ричной системе счисления (N<=10) длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

generate_numbers(4, 3)

# более простой пример для понимания
def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)

gen_bin(5)

# смотри лекции №8 (2017-2018) МФТИ "Алгоритмы на python"
def generate_permutations(N:int, M:int-1, prefix = None):
    """Генерация всех перестановок N чисел в М позициях,
    с префиксом prefix
    """
    M = N if M == -1 else M # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if number was in prefix: # FIXME
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()
