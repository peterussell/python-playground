class Superlist(list):
    def __len__(self):
        return 1000

superlist1 = Superlist()

print(len(superlist1))        # should always return 1000

superlist1.append('hello')
print(len(superlist1))

print(superlist1[0])
print(issubclass(Superlist, list))
