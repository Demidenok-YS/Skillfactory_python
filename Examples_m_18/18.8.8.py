# пусть a и b - переменные, которые мы хотим проверить
a = ""
b = ""
if (a and b) : # проверка истинности обеих переменных
    print("Обе переменные истинные")
    print(a,b)
elif (a or b) :
    print("Одна из переменных истинная")
    print(a or b)
else:
    print("Обе переменные ложные")