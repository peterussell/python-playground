# My attempt
def fib(num: int):
    current_sum = 0
    prev_sum = 0

    for i in range(num):
        if i == 0:
            yield [i, current_sum]
        elif i == 1:
            current_sum = 1
            yield [i, current_sum]
        else:
            new_sum = current_sum + prev_sum
            prev_sum = current_sum
            current_sum = new_sum
            yield [i, current_sum]


for i in fib(10):
    print(f'F{i[0]} = {i[1]}')

# ==========

# Instructor solution
# NB. IMPORTANT -- yield doesn't have to be the last thing in the function!
# it doesn't work like a return value, more like a "give this value back, but
# keep executing until the end"
def fib(num: int):
    a = 0
    b = 1
    for i in range(num):
        yield a
        
        tmp = a + b
        a = b
        b = tmp

for i in fib(10):
    print(i)


txt = " Hello World "
tmp = txt.strip()

print(tmp)
