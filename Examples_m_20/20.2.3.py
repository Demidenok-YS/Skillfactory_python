"""

Разберем задачу про поиск выхода из лабиринта.
Возможно, она покажется вам при первом подходе сложной и не очень к месту в этом уроке.
Однако, если вы всмотритесь в нее внимательно, то поймете, что она позволяет закрепить
работу с массивами и условными операторами, с функциями и циклами.

Задача звучит следующим образом:

Есть файл, в котором задан лабиринт.
В этом лабиринте буквой А отмечен вход. Буквой В отмечен выход, 0 — свободный проход, 1 — непроходимая стена.
Нужно составить и вывести на экран последовательность шагов (вверх, вниз, вправо, влево), которая приведет из точки
А в точку В.
Существует много разных алгоритмов поиска пути, разберем наиболее простой вариант — волновой алгоритм.

Идея в том, что начальной точке ставится вес — единица, затем от нее проверяется, можно ли пойти налево,
направо, вверх или вниз и в те места, где можно ставится вес на единицу больше. Затем перемещаем начальную
точку туда, куда мы смогли походить, и проверяем еще раз.

В итоге мы получаем вот такой лабиринт:
В котором -1 — это непроходимая стена, а остальные — это веса, которые символизируют, за сколько шагов
можно достичь этого места от начала лабиринта. Соответственно, путь строится от обратного: точка с выходом
принимается за начальную, и путь идет ровно по уменьшению веса — это будет минимально короткий выход из лабиринта.

Давайте посмотрим, как это реализовать в коде.

Это основа нашей программы. Что здесь происходит?

Мы читаем файл и подменяем значения из него для нашего удобства. Сначала читаем построчно,
убираем перевод строки и разбиваем строку на список. Мы будем работать с числами, так что нам нужно
заменить все стены на -1, чтобы они никак не участвовали в процессе, нолики остаются ноликами,
а начальная точка заменяется на единицу, конечная — на ноль, чтобы алгоритм также посчитал эту точку.
Кроме того, мы запоминаем позицию начала и конца в переменных pozIn и pozOut.

Затем у нас идёт условие, которое вызывает функцию. Посмотрим на функцию.

Здесь реализована логика, которая проверяет в матрице лабиринта, можно ли сходить
влево-вправо-вверх-вниз от точки, и если да, то этой точке присваивается текущий актуальный вес,
который увеличивается с каждым шагом.

Кроме того, каждый раз мы проверяем, не конечная ли точка, в которой мы оказались. И если мы в
какой-то момент ее достигнем, то функция прекратит выполняться и вернёт True, а если мы целиком
весь лабиринт так пройдем и не наткнёмся на выход, то вернёт False.

Итак, возвращаемся к рис.20.2.8. Условие у нас оценивает, что вернула функция, и если выхода
нет — печатает об этом сообщение, а если есть, то мы вызываем следующую функцию.

Эта функция похожа на предыдущую, она идет в обратную сторону и записывает, в какую сторону был выполнен шаг.

Опять возвращаемся к рис.20.2.8. Последний цикл for нужен просто для вывода получившегося лабиринта.
Итоговый вывод для этого конкретного лабиринта выглядит вот так:

"""


def found(pathArr, finPoint):
    weight = 1
    for i in range(len(pathArr) * len(pathArr[0])):
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == weight:
                    # Вниз
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight + 1

                        # Вверх
                    if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight + 1

                    # Вправо
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight + 1

                    # Влево
                    if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight + 1

                    # Конечная точка
                    if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                        pathArr[finPoint[0]][finPoint[1]] = weight + 1
                        return True
        weight += 1
    return False


def printPath(pathArr, finPoint):
    y = finPoint[0]
    x = finPoint[1]
    weight = pathArr[y][x]
    result = list(range(weight))
    while (weight):
        weight -= 1
        if y > 0 and pathArr[y - 1][x] == weight:
            result[weight] = 'Вниз'
            y -= 1
        elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
            result[weight] = 'Вверх'
            y += 1
        elif x > 0 and pathArr[y][x - 1] == weight:
            result[weight] = 'Вправо'
            x -= 1
        elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
            result[weight] = 'Влево'
            x += 1

    return result[1:]


labirint = []
with open("labirint.txt") as myFile:
    for line in myFile:
        labirint.append(line.replace('\n', '').split(' '))

ii = 0
for i in labirint:
    jj = 0
    for j in i:
        if j == 'A':
            labirint[ii][jj] = 1
            pozIn = (ii, jj)
        elif j == 'B':
            labirint[ii][jj] = 0
            pozOut = (ii, jj)
        elif j == '1':
            labirint[ii][jj] = -1
        else:
            labirint[ii][jj] = 0
        jj += 1
    ii += 1

if not found(labirint, pozOut):
    print("Путь не найден!")
else:
    result = printPath(labirint, pozOut)

    for i in labirint:
        for line in i:
            print("{:^3}".format(line), end=" ")
        print()
    print(result)