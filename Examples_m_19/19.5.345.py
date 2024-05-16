"""Задание 19.5.3
Напишите функцию D(a,b,c), возвращающую дискриминант квадратного уравнения.
Следующим этапом реализуем функцию, возвращающую «Нет вещественных корней», если дискриминант отрицательный.
Реализуйте функцию quadratic_solve(a,b,c), возвращающую «Нет вещественных корней» в случае отрицательного дискриминанта.
Далее модифицируем функцию таким образом, чтобы при нулевом дискриминанте возвращалось значение единственного корня.
Модифицируйте функцию quadratic_solve(a,b,c), чтобы она возвращала единственный корень при условии нулевого дискриминанта.
И последним этапом нам нужно вернуть сразу два значения. Конечный вид функции будет выглядеть так:"""

def D(a,b,c):
    return b**2 - 4*a*c
def quadratic_solve(a,b,c):
    if D(a,b,c) < 0:
        return "Нет вещественных корней"
    elif D(a,b,c) == 0:
        return -b/(2*a)
    else:
        return (-b-D(a,b,c)**0.5)/(2*a), (-b+D(a,b,c)**0.5)/(2*a)

print(quadratic_solve(1, 15, 26))
print(quadratic_solve(2, 3, 5))
print(quadratic_solve(1, 4, 4))
a = quadratic_solve(1, 15, 26)
print(type(a))