"""Задание 19.2.5
Дано натуральное число N. Вычислите сумму его цифр.

При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).

Задание 19.2.5

Здесь потребуется применить немного математики.
Алгоритм очень похожий: сумма цифр числа равна сумме последней цифры и
сумме остальных чисел:
сумма(2351)
    1 + сумма(235)
        5 + сумма(23)
            3 + сумма(2)
                2
            3 + 2
        5 + 5
    1 + 10
11

Главный вопрос здесь в том, как получать последнюю цифру числа,
и как получать число без последней цифры. И здесь вам пригодятся остаток от деления % и
целочисленное деление // на 10. Условие выхода из рекурсии — когда исходное число станет меньше 10.
Если число меньше 10, значит оно состоит из одной цифры, и для него уже не нужно искать сумму цифр."""

def sum2(num):
    if num < 10:
        return num
    return num % 10 + sum2(num // 10)

print(sum2(4234))