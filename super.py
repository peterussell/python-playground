class User:
    def __init__(self, name, email):
        # do some validation name and email that we don't
        # want to replicate for each subclass
        self.name = name
        self.email = email
	
    def get_contact_info(self):
        return f"Name: {self.name}, email: {self.email}"

# Option 1 -- User.__init__(self…)
class Wizard(User):
	def __init__(self, name, email, power_level):     # ← overrides User.__init__
		self.power_level = power_level
		User.__init__(self, name, email)

# Option 2 -- self().__init__(...)
class Archer(User):
	def __init__(self, name, email, num_arrows):
		self.num_arrows = num_arrows
		super().__init__(name, email)
		

w1 = Wizard("Merlin", "merlin@gmail.com", 20)
a1 = Archer("Robin", "robin@outlook.com", 100)

print(w1.get_contact_info())
print(a1.get_contact_info())

print(a1.__str__())
