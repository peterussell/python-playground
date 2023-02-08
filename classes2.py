"""Module representing a player character"""

class Player:
    """Represents a player class"""
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        """Returns the player's name"""
        return self._name

    def get_age(self):
        """Returns the player's age"""
        return self._age

    @classmethod
    def build_player(cls, name, age):
        """An example of how to build a player using a class ('cls') reference"""
        return cls(name, age)		# ← calls __init__

p1 = Player.build_player("Pete", 36)

print(f"p1: name={p1.get_name()}, age={p1.get_age()}")

# NB. we *can* override p1._name, but by convention we know this is private
# and shouldn't
