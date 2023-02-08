class User:
    def __init__(self: object, name: str) -> None:
        self.name = name

    def sign_in(self: object):
        print("Signed in")

class Wizard(User):
    def __init__(self: object, name: str, power_level: int):
        self.power_level = power_level
        User.__init__(self, name)

    def attack(self) -> None:
        print("attacking like a wizard")

class Archer(User):
    def __init__(self: object, name: str, num_arrows: int):
        self.num_arrows = num_arrows
        User.__init__(self, name)

    def attack(self) -> None:
        print("attacking like an archer")

    def check_arrows(self):
        print(f"{self.num_arrows} arrows remaining")

class HybridWarrior(Wizard, Archer):
    def __init__(self: object, name: str, power_level: int, num_arrows: int) -> None:
        Wizard.__init__(self, name, power_level)
        Archer.__init__(self, name, num_arrows)

hw = HybridWarrior("Reginald", 50, 3)
hw.attack()
hw.check_arrows()
hw.sign_in()
