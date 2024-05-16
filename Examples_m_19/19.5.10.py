"""Задание 19.5.10
Напишите рекурсивную функцию, которая зеркально разворачивает число.
Предполагается, что число не содержит нули."""


def mirror(a, res=0):
    if a == 0:
        return res
    else:
        return mirror(a // 10, res * 10 + a % 10)

ch = 1234
print(mirror(ch))