# A decorator to show how long a function takes to execute
from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()

        print(f"It took {t2 - t1}s")

        return result
    return wrapper

@performance
def long_time(numbers):
    for i in numbers:
        i * 5

long_time(range(1000000))
long_time(range(10000000))
long_time(range(100000000))
