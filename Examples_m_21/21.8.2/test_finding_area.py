from finding_area import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(f"Площадь прямоугольника с длиной {rect_1.a} и шириной {rect_1.b} : {rect_1.get_area()}")
print(f"Площадь прямоугольника с длиной {rect_2.a} и шириной {rect_2.b} : {rect_2.get_area()}")

square_1 = Square(5)
square_2 = Square(10)

print(f"Площадь квадрата со стороной  {square_1.a} : {square_1.get_area_square()}")
print(f"Площадь квадрата со стороной  {square_2.a} : {square_2.get_area_square()}")

circle_1 = Circle(3)
circle_2 = Circle(13)

print(f"Площадь круга с радиусом {circle_1.a} : {circle_1.get_area_circile()}")
print(f"Площадь круга с радиусом {circle_2.a} : {circle_2.get_area_circile()}")

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    elif isinstance(figure,Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circile())