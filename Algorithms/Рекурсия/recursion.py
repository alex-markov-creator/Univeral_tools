# Функция вычисления суммы - прием рекурсия
def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])  # Вызывает себя саму
print("SUMMA = ", mysum([23,53,-22,45,22,27,34,38,-62,91,22,41,-10,72,18,-21,34]))
# Функция вычисления факториала
def factorial(n):
    print(n)
    if n == 0:
        return 1
    return n * factorial(n-1)

print("FACTORIAL = ", factorial(4)) # 4 * 3 * 2 * 1 = 24
# Альтернативные варианты
def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])

print("SUMMA = ", mysum([1,2,3,4,5]))
#
def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)

print("SUMMA = ", mysum([1,2,15,4,5]))
# Косвенная рекурсия (вызывает функцию вызвавшую ее)
def mysum(L):
    if not L: return 0
    return nonempty(L)  #Вызов функции, которая вызовет эту функцию
def nonempty(L):
    return L[0] + mysum(L[1:])  #  Косвенная рекурсия
print("SUMMA = ", mysum([12,2,34,3,5 ]))
# ИНСТРУКЦИИ ЦИКЛОВ ВМЕСТО РЕКУРСИИ
L = [1,5,3,7,5, ]
sum = 0
while L:
    sum += L[0]
    L = L[1:]

print("SUMMA = ", sum)
# for
L = [9,8,7,6,5, ]
sum = 0
for x in L: sum += x
print("SUMMA = ", sum)
# factorial с помощью for
N = 5
factorial = 1
for x in range(1, N+1): factorial *= x
print("FACTORIAL = ", factorial)
# ОБХОД ВЛОЖЕННЫХ СПИСКОВ 
def sumtree(G):
    tot = 0
    for x in G: #Обход элементов одного уровня
        if not isinstance(x, list):
            tot += x    #Числа суммируются непосредственно
        else:
            tot += sumtree(x)   #Списки обрабатываются рекурсивными вызовами
    return tot

G = [1, [2, [3, 4], 5], 6, [7, 8]] # Произвольная глубина вложения
print ("SUMMA = ", sumtree(G))  #Выведет 36
print(sumtree([1, [2, [3, [4, [5]]]]])) # Выведет 15 (центр тяжести справа)
print(sumtree([[[[[1], 2], 3], 4], 5])) # Выведет 15 (центр тяжести слева)