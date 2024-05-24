"""

Напишите функцию count, которая возвращает количество вхождений элемента в массив
"""

def count(array, element):
    c = 0
    for i, a in enumerate(array):
        if a == element:
            c += 1
    return c

array = list(map(int, input().split()))
element = int(input())

print(count(array, element))