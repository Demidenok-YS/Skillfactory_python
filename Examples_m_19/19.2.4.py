"""Задание 19.2.4
С помощью рекурсивной функции разверните строку.

Задание 19.2.4

Разворот строки в какой-то степени напоминает подход в решению предыдущей задачи.
Когда справитесь с задачей 19.2.3, эта вам не покажется сложно.
Нужно с помощью рекурсии на каждом этапе переставлять последнюю букву в начало.
Развёрнутая строка — это последний символ строки, к которому справа добавили развёртную часть остальной строки:
развернуть("привет")
    "т" + развернуть("приве")
        "е" + развернуть("прив")
            "в" + развернуть("при")
                "и" + развернуть("пр")
                    "р" + развернуть("п")
                        "п"
                    "р" + "п"
                "и" + "рп"
            "в" + "ирп"
        "е" + "вирп"
    "т" + "евирп"
"тевирп"

Условием выхода здесь станет последняя буква в слове,
потому что когда слово состоит из одной буквы, его уже не требуется разворачивать."""

def reverse_str(text):
    if len(text) == 0:
        return " "
    return text[-1] + reverse_str(text[:-1])

print(reverse_str("полигель"))