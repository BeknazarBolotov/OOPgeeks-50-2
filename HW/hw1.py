

import random

class Hero:

    def __init__(self, name, lvl=1, hp=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp


    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl} , мое HP {self.hp}.")


    def is_adult(self):
        if self.lvl >= 10:
            return True
        else: return False


    def __str__(self):
        return f"Имя: {self.name}, Уровень: {self.lvl}, Жизнь: {self.hp}"


    def rest(self):
        self.hp = random.randint(0, 100)

        return print(f"{self.name} rest and reset hp {self.hp}")



# hero1 = Hero("Guts", 100, 1000)
# hero2 = Hero("Grifith", 50, 10000)
# hero3 = Hero("Casca", 9, 75)
#
#
# print(hero1.is_adult())
# hero2.introduce()
# print(hero3)
