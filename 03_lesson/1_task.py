import random
from time import time


def repeater(repeats):

    def decorator(func):

        def wrapper():
            start_time = time()
            results = []

            for repeat in range(repeats):
                print(repeat)
                results.append(func())

            print(f'funck take for {round(time() - start_time, 4)} second')
            return results
        return wrapper
    return decorator


@repeater(15)
def get_random():
    result = 1
    for _ in range(5):
        result += random.randint(1, 10 +1)
    return result


#print(repeater(30)(get_random)(10, 300))
print(get_random())