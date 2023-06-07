# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def sum(a, b):
    if a < b or b > 0:
        return sum(a + 1, b - 1)
    return a, b

print('Enter first number')
a = int(input())
print('Enter second number')
b = int(input())

print(sum(a, b))