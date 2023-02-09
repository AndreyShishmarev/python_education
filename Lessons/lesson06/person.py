class Human:
    age: int
    first_name: str
    last_name: str
    weight: int

    counter: int = 0
    def __init__(self, first_name, last_name, age, weight=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        Human.counter += 1

    def info(self):
        print(f"I'm {self.first_name}, age:{self.age}, weight: {self.weight}")


john = Human("John", "Doe", 30)
artur = Human("Artur", "Doe", 40)

john.info()
artur.info()
print(john.counter)
print(artur.counter)
print(Human.counter)

# print(john, artur)

# john.age = 30
# john.first_name = "John"
# john.last_name = "Doe"
#
# artur.age = 40
# artur.first_name = "Artur"
# artur.last_name = "Doe"

# print(john.first_name, john.last_name, john.age, john.weight)
# print(artur.first_name, artur.last_name, artur.age, john.weight)

# person_dict = {"age": 0, "first_name": "", "last_name": ""}

# john.info()
# Human.info(john)
