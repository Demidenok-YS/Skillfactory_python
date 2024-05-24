"""
В нашей структуре данных, в каждом узле бинарного дерева мы будем хранить указатель на левого и правого потомка.

Мы создали класс узла, а в конструкторе записали значение, которое должно храниться в нём. Также инициализировали
левого и правого потомка. Пока что в них ничего не хранится — нужно иметь процедуру вставки новых элементов.
Напишем разные методы для вставки на место левого потомка и на место правого потомка.

Поясним, что здесь произошло. Если в текущем узле нет левого потомка, то новый узел вставляем на его место.
Если левый потомок уже существует — он становится таким же левым потомком, но уже нового узла.
Иными словами, он остается левым, но его глубина увеличивается. Аналогично поступим с правым.

В обоих случаях мы возвращаем ссылку на текущий узел. Это нам необходимо, чтобы создавать цепочки действий.

В одной строчке мы создали корневой узел дерева, вставили левого потомка и затем — сразу правого.
Получая ссылки на потомков через атрибуты left_child и right_child, можно проделать ту же самую цепочку
действий, чтобы расширить дерево.


"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self


A_node = BinaryTree('A').insert_left('B').insert_right('C')

# создаём корень и его потомков /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)


