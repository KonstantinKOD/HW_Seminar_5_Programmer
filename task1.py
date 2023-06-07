# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую
# степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def rec(a, b):
    if b > 0:
        return a * rec(a, b - 1)
    return 1

print('Enter number')
a = int(input())
print('Enter degree of number')
b = int(input())

print(rec(a, b))
