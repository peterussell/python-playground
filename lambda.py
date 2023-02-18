from functools import reduce

# see map_filter_zip_reduce.py for original examples
my_list = [1,2,3]


# map example using lambda instead of def multiply_by_2
doubled_list = list(map(lambda item: item * 2, my_list))

print(doubled_list)


# == filter example using lambda ==
to_100 = list(range(1, 101))
evens_only = list(filter(lambda item: item % 2 == 0, to_100))
print(evens_only)

# == reduce example using lambda ==
to_10 = list(range(1, 11))
summed = reduce(lambda acc, val: acc + val, to_10)
print(summed)
