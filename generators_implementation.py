# implementing a for loop
def special_for(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(next(iterator) * 2)
        except StopIteration:
            break

special_for([1,2,3])


# implementing the range function
class MyGen:
    current = 0

    def __init__(self, first, last) -> None:
        MyGen.current = first
        self.last = last

    def __iter__(self) -> any:
        return self
    
    def __next__(self) -> int:
        if (MyGen.current < self.last):
            num = MyGen.current
            MyGen.current += 1
            return num
        
        raise StopIteration
    
gen = MyGen(10, 50)
for i in gen:
    print(i, end=", ")

print()
