

class Heroes:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return print(f"{self.name} борется с врагами!")

    def attack(self):
        return print(f"{self.name} выстрелил из своего лука!")


class Archer(Heroes):

    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision


    def attack(self):
        self.arrows -= 1
        print(f"{self.name} потратил одну стрелу. Осталось стрел: {self.arrows}")
        if self.precision > 10:
            print(f"{self.name} попал в цель!")
        else:

            print(f"{self.name} не попал в цель😭")



    def rest(self):
        self.arrows += 5
        print(f"{self.name} отдохнул и набрался сил. +5 стрел")


    def status(self):
        print(f"{self.name}, Здоровье: {self.hp}, Кол-во стрел: {self.arrows}, Точность: {self.precision}")


guts = Archer("Guts", 100, 10, 5)
guts.action()
guts.attack()
guts.status()
guts.rest()