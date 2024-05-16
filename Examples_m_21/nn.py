class User:
    pass
peter = User()                      #создания экземпляра класса
peter.name = "Peter Robertson"      #сохранить в экземпляре какие-то данные

julia = User()                      #создания экземпляра класса
julia.name = "Julia Donaldson"      #сохранить в экземпляре какие-то данные

print(peter.name)
print(julia.name)

peter.email = "peterrobertson@mail.com"
print(peter.email)
print('\n')
print(julia.email)