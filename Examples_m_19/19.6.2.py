"""Задание 19.6.2
Отфильтруйте из заданного списка только четные элементы.

[-2, -1, 0, 1, -3, 2, -3] """

def chet(x):
    return x % 2 == 0

res = filter(chet, [-2, -1, 0, 1, -3, 2, -3])
print(list(res))