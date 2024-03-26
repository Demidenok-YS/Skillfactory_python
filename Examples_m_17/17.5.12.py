"""Напишите программу, которая на вход принимает текст и
выводит количество уникальных символов."""

text = input("Input text:")
rez = list(set(text))
print("kol-vo unik simvols:", len(rez))