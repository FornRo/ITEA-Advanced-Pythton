import random
from time import time


def repeater(repeats):

    def decorator(func):

        def wrapper():
            start_time = time()
            results = []

            for i in range(repeats):
                results.append(func())

            print(f'funck take for {round(time() - start_time, 4)} second')
            return results
        return wrapper
    return decorator


@repeater(15)
def get_random():
    result = 1
    for _ in range(5):
        result *= random.randint(1, 100 +1)
    return result


#print(repeater(30)(get_random)(10, 300))
print(get_random())