"""
 Задание 21.8.2
Выполните задание, взяв за основу полученный код из задания 21.8.1.
Добавьте еще один класс — круг (class Circle), который принимает в качестве аргументов свой радиус.

Вычислите площадь круга (π × r2).

Опубликуйте код на Github, призовите в Slack ментора для проверки и консультации.

"""

import math

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2

class Circle:
    def __init__(self, a):
        self.a = a

    def get_area_circile(self):
        return math.pi * self.a ** 2


