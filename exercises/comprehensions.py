# Return a list containing duplicates in the given list
orig_vals = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({x for x in orig_vals if orig_vals.count(x) > 1})

print(duplicates)
