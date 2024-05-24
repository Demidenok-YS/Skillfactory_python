"""
Задание 22.9.1 (HW-03)
Напишите программу, которой на вход подается последовательность чисел через пробел, а также
запрашивается у пользователя любое число.
В качестве задания повышенного уровня сложности можете выполнить проверку соответствия
указанному в условии ввода данных.

Далее программа работает по следующему алгоритму:

1) Преобразование введённой последовательности в список
2) Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
3) Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий
 за ним больше или равен этому числу.
При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен
в этом модуле. Реализуйте его также отдельной функцией.

Подсказка
Помните, что у вас есть числа, которые могут не соответствовать заданному условию. В этом случае
необходимо вывести соответствующее сообщение

"""
import random
def q_sort(array):
    if len(array) > 1:
        temp = array[random.randint(0, len(array)- 1)]
        left = [i for i in array if i < temp]
        eq = [i for i in array if i == temp]
        right = [i for i in array if i > temp]

        array = q_sort(left) + eq + q_sort(right)
    return array

def search_indices(array, N, left, right):
    if left > right:
        return False
    middle = (left + right) // 2
    if array[middle] < N and array[middle + 1] >= N:
        return f"Индекс элемета, который меньше введенного значения ({N}): {middle}"
    elif N <= array[middle]:
        return search_indices(array, N, left, middle -1)
    else:
        return search_indices(array, N, middle + 1, right)

try:
    list_array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
    sort_list_array = q_sort(list_array)
    print("Список последовательности: ")
    print(sort_list_array)
    search_element = int(input("Введите любое число: "))
    if search_element < sort_list_array[0] or search_element > sort_list_array[-1]:
        print("Введенное число не соответствует заданному условию.")
    else:
        print(search_indices(sort_list_array, search_element, 0, len(sort_list_array) - 1))

except ValueError as v:
    print(f"Необходимо вводить числа.")






