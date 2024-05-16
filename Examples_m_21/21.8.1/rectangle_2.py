# Импорт классов
from Rectangle import Rectangle, Square

# Добавление обьектов
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(f"Площадь прямоугольника с длиной {rect_1.a} и шириной {rect_1.b} : {rect_1.get_area()}")
print(f"Площадь прямоугольника с длиной {rect_2.a} и шириной {rect_2.b} : {rect_2.get_area()}")

square_1 = Square(5)
square_2 = Square(10)

print(f"Площадь квадрата со стороной  {square_1.a} : {square_1.get_area_square()}")
print(f"Площадь квадрата со стороной  {square_2.a} : {square_2.get_area_square()}")
# print(square_1.get_area_square(), square_2.get_area_square())

# Создание коллекции
figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())