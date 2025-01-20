# # 1 Декоратор без аргументов
#
# def simple_dec(func): # 2 второй шаг - создание декоратора
#
#     def wrapper(): # 3 третий шаг - создание обертки
#         print("start") # 5 четвертый шаг - вызов декорируемой функции
#         func()
#         print("end")
#     return wrapper # 4 четвертый шаг - вызов декорируемой функции
#
# @simple_dec # Первый шан - вызов декоратора
# def print_text():
#     print("text")
#
# print_text()
#
#
#
# # 2 Декортатор с аргументами
#
# def greeting_dec(func):
#
#     def wrapper(name):
#         print("Hi", name)
#         func(name)
#         print("goodbye", name)
#     return wrapper
#
#
# @greeting_dec
# def say_hello(name):
#     print("hello", name)
#
# say_hello("John")



class MyAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return MyAdd(self.a + other.a, self.b + other.b)

    def __gt__(self, other):
        pass
