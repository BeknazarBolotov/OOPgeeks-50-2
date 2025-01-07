# from main import Hero
#
# kirito = main.Hero("Kirito", 100)
#
# kirito.is_adult()


# Наследование
# Полиморфизм


# Дочерний класс
# Родительский класс


from hw1 import Hero

class ShieldHero(Hero):
    def __init__(self,name, lvl=1, hp=100, mp=100):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"{self.name} берёт щит и защищается"


hr = ShieldHero("Наофуми")
hr.introduce()
hr.action()

