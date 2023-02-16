from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

capitalized_pets = list(map(str.capitalize, my_pets))
print(capitalized_pets)


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort()
combined = list(zip(my_strings, my_numbers))
print(combined)

def is_over_50(val: int) -> bool:
    return val > 50

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
passes = list(filter(is_over_50, scores))
print(passes)


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc: int, item: int) -> int:
    return acc + item

my_numbers.extend(scores)

total = reduce(accumulator, my_numbers)
print(total)
