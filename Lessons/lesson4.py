# from Mypackage import add
#
# print(add(1, 2))
#
# import tkinter
# tkinter.Tk()
# tkinter.Button()
#
# import sys
# from colorama import init, Fore, Back, Style
#
#
# init()
#
# print(Fore.RED + "Hello World!")
from http.cookiejar import join_header_words


# class MyClass:
#
#
#     def instance_method(self):
#         print("instance method")
#




class MyClass:


    @classmethod
    def class_method(cls):
        print("class method")


obj = MyClass()
obj.class_method()


