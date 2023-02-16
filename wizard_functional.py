# Keeps data and functions separate

wizard = {
    "name": "Merlin",
    "power": 50
}

def attack(character) -> str:
    return f"{character['name']} is attacking with power {character['power']}"

print(attack(wizard))
