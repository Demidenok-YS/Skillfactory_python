"""Задание 20.1.3

Выполните код, как на рисунке 20.1.2. Откройте только что созданный файл."""

myFile = open('name.txt', 'w')
myFile.write('ttttt')
print('zzzzz', file=myFile)