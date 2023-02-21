from time import time

def performance(fn):
    def wrapper():
        t1 = time()
        fn()
        t2 = time()
        print(f"Execution time: {t2-t1}")

    return wrapper

nums = 10000000

# this function just uses a generator (no list)
@performance
def long_time_generator():
    print('1')
    for i in range (nums):
        i * 5

# this function converts the range to a list before iterating over it
@performance
def long_time_list():
    print('2')
    for i in list(range(nums)):
        i * 5

long_time_generator()   # Execution time: 0.5697422027587891
long_time_list()        # Execution time: 1.1018061637878418