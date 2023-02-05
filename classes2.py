class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def build_player(cls, name, age):
        return cls(name, age)		# ← calls __init__

p1 = Player.build_player("Pete", 36)

print(f"p1: name={p1.name}, age={p1.age}")
