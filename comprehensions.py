# manual way without comprehensions
the_chars = []

for char in 'hello':
    the_chars.append(char)

print(the_chars)


# using comprehension instead
new_chars = [char for char in 'hello']
print(new_chars)

to_100 = [num for num in range(100)]
print(to_100)

# altering the value stored in the list
doubled_to_10 = [(num * 2) for num in range(10)]
print(doubled_to_10)

# with a condition for whether to include in the result
conditionals = [val+101 for val in range(10) if val % 2 == 0]
print(conditionals) # [102, 104, 106, 108, 110]


# == SET comprehrensions ==
odd_nums_set = {num + 10 for num in range(10) if num % 2}
print(odd_nums_set) # {11, 13, 15, 17, 19}

# won't add duplicates
no_duplicates_comprehension = {num for num in [1,1,2,2,2,3,3,3,4,4,4]}
print(no_duplicates_comprehension) # {1, 2, 3, 4}


# == DICTIONARY comprehensions ==
orig_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

squared_dict = {key:val**2 for key,val in orig_dict.items()}
print(squared_dict) # {'a': 1, 'b': 4, 'c': 9}

changed_keys = {f"key_{key}":val**2 for key,val in orig_dict.items()}
print(changed_keys) # {'key_a': 1, 'key_b': 4, 'key_c': 9}

# Common to shorten to 'k' and 'v'
new_dict = {k:v*10 for k,v in orig_dict.items()}
print(new_dict) # {'a': 10, 'b': 20, 'c': 30}

# Can still use conditionals with dictionary comprehensions
cubed_evens = {k:v**3 for k,v in orig_dict.items() if v%2}
print(orig_dict) # {'a': 1, 'b': 2, 'c': 3}
print(cubed_evens) # {'a': 1, 'c': 27}


# == Creating keys ==
created_keys = {v:v**2 for v in [1,2,3]}
print(created_keys) # {1: 1, 2: 4, 3: 9}
