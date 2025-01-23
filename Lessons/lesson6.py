class Animal:
    pass

class Flyable:

    def fly(self):
        return print("I'm flying")


class Swimmable:

    def swim(self):
        return print("I'm swimming")


class Duck(Flyable, Swimmable):
    def make_sound(self):
        return print("Making sound")

donald_duck = Duck()

donald_duck.fly()
donald_duck.swim()
donald_duck.make_sound()