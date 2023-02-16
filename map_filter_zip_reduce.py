from functools import reduce

# == map ==
def multiply_by_2(val: int) -> int:
    return val * 2

orig_vals = [1,2,3,4,5]
doubled_vals = list(map(multiply_by_2, orig_vals))

print(orig_vals)
print(doubled_vals)

# == filter ==
def is_odd(val: int) -> bool:
    return val % 2

def is_even(val: int) -> bool:
    return not is_odd(val)

nums = list(range(40))
odd_nums = list(filter(is_odd, nums))
even_nums = list(filter(is_even, nums))

print(nums)
print(odd_nums)
print(even_nums)

# == zip ==
my_list = [1,2,3]
your_list = [20,30,40]

zipped_list = list(zip(my_list, your_list))
print(zipped_list) # [(1, 20), (2, 30), (3, 40)]

# given a single iterable, creates tuples with single item
single_zipped_list = list(zip(my_list))
print(single_zipped_list) # [(1,), (2,), (3,)]

my_list.append(4)
my_list.append(5)

# given uneven length iterables, creates tuples up to the length of the shortest
uneven_zipped_list = list(zip(my_list, your_list))
print(uneven_zipped_list) # [(1, 20), (2, 30), (3, 40)]

# == reduce ==
# from functools import reduce
one_to_five = list(range(5, 10))

def accumulator(acc: int, item: int) -> int:
    print(f"accumulator: {acc}, item: {item}")
    return acc + (item if is_even(item) else 0)

reduced_val = reduce(accumulator, one_to_five, 10)

print(reduced_val)

# accumulator: 5, item: 6
# accumulator: 11, item: 7
# accumulator: 11, item: 8
# accumulator: 19, item: 9
# 19