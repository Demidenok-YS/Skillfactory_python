"""Написать функцию, которая будет перемножать любое количество переданных ей аргументов."""

def divide(*nums):
    p = 1
    for i in nums:
        p *= i
    return p

print(divide())
print(divide(2,3))
print(divide(1,2,3,4))