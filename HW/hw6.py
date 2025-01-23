class Cars:
    def show(self):
        print("I am a car!")

class Toyota(Cars):
    def toyota_car(self):
        print("I am a Japanese car - Toyota!")

class BMW(Cars):
    def bmw_car(self):
        print("I am a German car - BMW!")
class Mersedes(Toyota, BMW):
    def mers_car(self):
        print("I am the best car!")

obj = Mersedes()

obj.show()
obj.toyota_car()
obj.bmw_car()
obj.mers_car()
