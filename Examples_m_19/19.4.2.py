"""Задание 19.4.2

Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
Для хранения переменной, содержащей количество вызовов, используйте nonlocal область декоратора."""

def counter(func):
   count = 0
   def wrapper(*args, **kwargs):
       nonlocal count
       func(*args, **kwargs)
       count += 1
#       print(f"Функция {func} была вызвана {count} раз")
       print(count)
   return wrapper

@counter
def say_word(word):
   print(word)

say_word("Oo!!!")
say_word("Oo!!!")