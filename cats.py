#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cats = []
cats.append(Cat("Meowgli", 10))
cats.append(Cat("FluffnStuff", 3))
cats.append(Cat("Scar", 27))

# 2 Create a function that finds the oldest cat
def find_oldest(all_cats: list) -> Cat:
    """Returns the oldest cat in a given list, or None if the list is empty"""
    oldest_cat = None

    for cat in all_cats:
        if (oldest_cat is None) or (cat.age > oldest_cat.age):
            oldest_cat = cat

    return oldest_cat

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_cat = find_oldest(cats)
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")
