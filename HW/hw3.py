import random
from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.__random_int = random.randint(1, 3)  # Приватный атрибут

    def attack(self):
        print(f"{self.name} attacks the enemy!")

    def protection(self):
        print(f"{self.name} defends against the attack!")

    def rest(self):
        self.hp += 15
        print(f"{self.name} takes a rest to recover health. {self.hp}")

    def get_random_int(self):
        return self.__random_int  # Доступ к приватному атрибуту

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass


class Jester(Hero):
        def unique_attack(self):
            # Логика уникальной атаки: атака с неожиданным поворотом
            print(f"{self.name} performs a tricky somersault and throws a surprise attack!")

        def unique_scream(self):
            print(f"{self.name} shouts: Is that all you've got? Let's dance!")

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

hero = Jester("Jester", 100, 100)
hero.unique_attack()
hero.unique_scream()
hero.action()
hero.rest()