"""
1) Итак, у нас есть класс Rectangle с двумя параметрами: ширина и высота (a и b).
Мы можем найти площадь прямоугольника. Для этого нужно ширину умножить на высоту.
Для решения используем специальный метод get_area. Он принимает аргумент self, то есть сам класс Rectangle,
и возвращает произведение атрибута a (ширина) на b (высота).

2) Создадим файл rectangle_2.py в отдельной директории в папке (назовем её python_practice).
Выполним импорт класса Rectangle. Создадим 2 прямоугольника и выведем их площади.

3) Добавим в нашу программу еще один класс, например Square (квадрат), который принимает
в качестве аргумента одну сторону. Добавляем данные в исходный файл rectangle.py

4) Переходим в файл rectangle_2.py и импортируем наш новый класс.

5) (Работаем в файле rectangle_2.py) Теперь мы хотим в нашей программе все объекты перенести в единую коллекцию.
Назовем фигуры (figures). Коллекция содержит список, в который мы помещаем наш первый прямоугольник,
квадрат и т.д. (см 17 строчку).
Далее пройдемся по циклу for. Это необходимо, чтобы найти площадь каждой фигуры, сохраненной в списке figures.
Обратите внимание, мы будем работать с прямоугольниками и квадратами с помощью разных методов:
get_area() и get_area_square().
Внутри цикла проверяем:
Если экземпляр класса figure является квадратом, то вызываем метод get_area_square().
В противном случае — обрабатываем данные для прямоугольника методом get_area().
В условии есть функция isinstance, поддерживающая наследование.
Она проверяет, является ли аргумент объекта экземпляром класса или экземпляром класса из кортежа.
В случае если является, функция возвращает True, если не является — False.

"""

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