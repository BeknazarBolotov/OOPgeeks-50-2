import random
from abc import ABC, abstractmethod


class Hero:
    def __init__(self, name, lvl, hp, protection):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.__random_int = random.randint(0, 3)


    def attack(self):
        return print(f"{self.name} атакует!")

    def protection(self):
        return print(f"{self.name} защищается")

    def rest(self):
        self.hp += 15
        return print(f"{self.name} отдохнул и восполнил здоровье!")

    def get_random_int(self):
        pass

    @abstractmethod
    def unique_attack(self):
        return print(f"{self.name} выполняет сальто и наносит внезапный удар!")

    @abstractmethod
    def unique_scream(self):
        return print(f"{self.name} shouts: Is that all you've got? Let's dance!")

    @abstractmethod
    def action(self):
        action_type = self.get_random_int()
        if action_type == 1:
            self.attack()
        elif action_type == 2:
            self.protection()
        elif action_type == 3:
            self.rest()
        else:
            print("Unexpected action!")


from hw3 import Hero

class Jester(Hero):
