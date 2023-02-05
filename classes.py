"""Module representing a player character"""

class Player:
    has_membership = True
    """Class representing a player"""

    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def print_rules(cls, print_short=True):
        if print_short:
            print("Here are the short rules")
        else:
            print("These are really really long rules. They take a long time to read.")

    def run(self):
        """Runs the game"""
        print(f"Hello {self.name}, welcome to the game.")

# don't need an object to use @classmethods or attributes
Player.print_rules(False)
print(f"Do all players have memberships? {Player.has_membership}")

p1 = Player("Pete")
print(f"p1.has_membership (class attribute) = {p1.has_membership}")
p1.has_membership = False    # setting the instance attribute has_membership
print(f"p1.has_membership (instance attribute) = {p1.has_membership}")
print(f"p1.has_membership (instance attribute) = {p1.has_membership}")
print(f"Player.has_membership (class attribute) = {Player.has_membership}")

p2 = Player("Gustav")
p2.has_membership = False

print(p1.has_membership)

p1.has_membership = False
print(p1.has_membership)
# print(Player.has_membership)
