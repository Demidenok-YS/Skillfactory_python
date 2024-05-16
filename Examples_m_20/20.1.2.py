"""Задание 20.1.2
Создайте текстовый файл filename.txt с вашей любимой песней (вручную, через проводник)
и попробуйте вывести содержимое целиком и построчно с помощью методов, рассмотренных выше.

print(myFile.read())
print(myFile.readline(40))
for line in myFile:
    print(line)
    """


myFile = open('filename.txt', 'rt', encoding="utf8")
for line in myFile:
    print(line)
