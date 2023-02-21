def generator_function(num):
    for i in range(num):
        yield i

# nb. this is what's happening under the hood when we iterate
g = generator_function(10)

print(next(g))    # '0'
next(g)
next(g)
next(g)
print(next(g))    # '4'

# but we can use it with built in iterators like the for loop
# nb. the iterate will pick up from wherever g is up to
for item in g:
    print(item, end=",")    # '5,6,7,8,9,'

print()



# == StopIteration error ==
# Occurs when we try to iterate more times than the number of items in the iterable
def gen2(num):
    for i in range(num):
        yield f'This is number {i}'

g2 = gen2(1) # only has 1 iteration

print(next(g2))
next(g2)           # 'Traceback (most recent call last): ... StopIteration'
