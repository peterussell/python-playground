from functools import reduce

# print squares
my_list = [5,4,3]
print(list(map(lambda val: val * val, my_list)))

# sort list of tuples (sort based on 2nd value)
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a) # [(10, -1), (0, 2), (4, 3), (9, 9)]
