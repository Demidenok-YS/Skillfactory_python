""""У вас есть заготовка функции — def get_wind_class(speed).
Вам нужно вместо ??? написать код, который возвращает из функции
класс ветра в зависимости от его характера:
от 1 до 4 м/с включительно - "weak [1]"
от 5-10 м/c - "moderate [2]"
от 11-18 м/c - "strong [3]"
от 19 м/c - "hurricane [4]"
def get_wind_class(speed):
     ???"""

def get_wind_class(speed): #объявление функции
    if 1 <= speed <= 4: #только аргумент
        return "weak [1]"
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return"strong [3]"
    elif speed >= 19:
        return "hurricane [4]"
print(get_wind_class(3)) #мы просим программу напечатать то, что в скобках