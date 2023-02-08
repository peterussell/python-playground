class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):            # overrides Toy.__str__()
        return f"I am a {self.color} toy that is {self.age} years old"

my_toy = Toy("red", 0)

print(str(my_toy))


# Overriding __call__
class RocketShip(Toy):
    def __call__(self):
        return "Yesss? You called?"

rocket = RocketShip("silver", 2)
print(rocket())


# Overriding __getitem__
class Person:
    def __init__(self):
        self.metadata = {
            "name": "Pete",
            "age": 100
        }

    def __getitem__(self, key):
        return self.metadata[key]

my_person = Person()
print(my_person['age'])	# '100'
