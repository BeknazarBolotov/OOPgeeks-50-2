#OOP


# First class

# add_number
# AddNumber


class Person:


    # Магический метод

    def __init__(self, name, age=0, city="None"):
        # Атрибуты класса
        self.name = name
        self.age = age
        self.city = city


    def introduce(self):
        print(f"Привет меня зовут {self.name}. Мне {self.age} лет. Я живу в городе {self.city}.")


    def __str__(self):
        return f"Вернул имя объкта {self.name}"



# Объекты класса (экзепляры класса)
person_first = Person("Бекназар", 16, "Бишкек")
person_second = Person(name="John Doe", age=33, city="None")


print(person_second.age)
person_first.introduce()
print(person_second)
