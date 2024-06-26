"""Создайте скрипт, который будет в input() принимать строки,
их необходимо будет конвертировать в числа, добавьте try-except,
чтобы строки могли быть сконвертированы в числа.

В случае удачного выполнения скрипта пусть выведется: «Вы ввели правильное число».
В конце скрипта обязательно должна быть надпись «Выход из программы».
ПРИМЕЧАНИЕ: Для отлова ошибок используйте try-except, а также блоки finally и else."""


try:
    str1 = int(input())
except ValueError as error:
    print("Вы ввели неправильное число")
else:
    print(f"Вы ввели {str1}")
finally:
    print("Выход из программы")
