"""Задание 19.6.1
C помощью метода строки str.lower переведите все элементы списка в нижний регистр.

L = ['THIS', 'IS', 'LOWER', 'STRING']"""

L = ['THIS', 'IS', 'LOWER', 'STRING']
STR = ' '.join(L)                       #преобразование списка в строку
STR = STR.lower()                       #применяем метод lower
STR_1 = list(STR.split())               ##преобразование строку в список
print(STR_1)

print(list(map(str.lower, L)))
# ['this', 'is', 'lower', 'string']