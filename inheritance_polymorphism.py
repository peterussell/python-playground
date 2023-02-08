from abc import ABC, abstractmethod

class User:
    def sign_in(self) -> None:
        print("You are signed in")

    @abstractmethod       # allows more strongly-typed polymorphism
    def attack(self):
        pass

class Wizard(User):
    def __init__(self, name: str, power_level: int) -> None:
        self._name = name
        self._power_level = power_level

    def attack(self):
        print(f"Wizard attack with power level {self._power_level}")

class Archer(User):
    def __init__(self, name: str, num_arrows: int) -> None:
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        self._num_arrows -= 1
        print(f"Archer attack, number of arrows left: {self._num_arrows}")

w1 = Wizard("Merlin", 50)
a1 = Archer("Robin", 100)

print(f"Is wizard 1 a Wizard? {isinstance(w1, Wizard)}")
print(f"Is wizard 1 a User? {isinstance(w1, User)}")
print(f"Is wizard 1 an Archer? {isinstance(w1, Archer)}")
print(f"Is wizard 1 an object? {isinstance(w1, object)}")

print("Time to attack!")
w1.attack()
a1.attack()
w1.attack()
a1.attack()
a1.attack()
a1.attack()
a1.attack()
w1.attack()
