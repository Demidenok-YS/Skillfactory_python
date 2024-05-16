"""Напишите функцию, которая будет возвращать количество делителей числа а.

Пример ввода: 5

Пример вывода программы: 2
"""

def kolvo_del(a):
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
    return count
print(kolvo_del(6))