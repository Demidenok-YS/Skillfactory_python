"""
Попробуем создать обработчик задач на бесконечном цикле с использованием очереди:
1) в первую очередь реализуем проверку наличия элементов в очереди.
2) Напишите функцию is_empty, которая проверяет наличие элементов в очереди,
используя указатели head и tail. Запрещается использование функции len(list_), так как её сложность O(n).
3)Напишите функцию size, которая возвращает текущий размер очереди. Учтите, что необходимо рассмотреть
несколько случаев: когда очередь пустая, когда очередь полная (какому условию соответствует?),
а также отдельное внимание стоит обратить на тот случай, когда хвост очереди переместился
в начало списка (закольцевался).
4) Напишите функцию add, которая добавляет задачу в конец очереди. Также учтите, что размер массива ограничен,
 и при достижении этого предела необходимо перенести указатель в положение 0. Также обратите внимание на
 области видимости переменных tail и order. После добавления задачи в очередь, она должна вывести уведомление
  об этом в формате:

"Задача №1 добавлена"

5)Напишите функцию, печатающую информацию о приоритетной задаче в формате:

"Задача №1 в приоритете"

6) def show(): # выводим приоритетную задачу

7) Напишите функцию, которая печатает в консоль задачу (=выполняет её) и, соответственно,
удаляет её из очереди, присваивая ей значение 0. Формат вывода:

"Задача №1 выполнена"

"""

N_max = int(input("Определите размер очереди:"))

queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
order = 0  # будем хранить сквозной номер задачи
head = 0  # указатель на начало очереди
tail = 0  # указатель на элемент следующий за концом очереди

def is_empty(): # очередь пуста?
    # да, если указатели совпадают и в них содержится ноль
    return head == tail and queue[head] == 0
def size(): # получаем размер очереди
    if is_empty(): # если она пуста
        return 0 # возвращаем ноль
    elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
        return N_max # значит очередь заполнена
    elif head > tail: # если хвост очереди сместился в начало списка
        return N_max - head + tail
    else: # или если хвост стоит правее начала
        return tail - head


def add():  # добавляем задачу в очередь
    global tail, order
    order += 1  # увеличиваем порядковый номер задачи
    queue[tail] = order  # добавляем его в очередь
    print("Задача №%d добавлена" % (queue[tail]))

    # увеличиваем указатель на 1 по модулю максимального числа элементов
    # для зацикливания очереди в списке
    tail = (tail + 1) % N_max

def show(): # выводим приоритетную задачу
    print("Задача №%d в приоритете" % (queue[head]))

def do(): # выполняем приоритетную задачу
    global head
    print("Задача №%d выполнена" % (queue[head]))
    queue[head] = 0 # после выполнения зануляем элемент по указателю
    head = (head + 1) % N_max # и циклично перемещаем указатель


while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", size())
    elif cmd == "add":
        if size() != N_max:
            add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if is_empty():
            print("Очередь пустая")
        else:
            show()
    elif cmd == "do":
        if is_empty():
            print("Очередь пустая")
        else:
            do()
    elif cmd == "exit":
        for _ in range(size()):
            do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")

