"""
Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
Вам необходимо написать программу, которая позволит составить список гостей.
В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.

Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

"""
class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def get_info(self):
        return f"{self.name} {self.surname}. г. {self.city}."

user_1 = Client("Ярослав", "Ростовцев", "Владимир", 10000)
user_2 = Client("Александр", "Крот", "Москва", 33000)
user_3 = Client("Ева", "Польна", "Москва", 120500)
user_4 = Client("Виктория", "Смирнова", "Ковров", 85500)

clients = [user_1, user_2, user_3, user_4]
for client in clients:
    print(client.get_info())