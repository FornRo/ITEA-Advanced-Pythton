from time import time

def repeater_fib(repeats):
    def decorator(func):
        start_time = time()
        
        def wrapper(n):
            results = 0
            for _ in range(repeats):
                results += func(n)
            print(f'funck take for {round(time() - start_time, 4)} second')

            return results
        return wrapper
    return decorator


@repeater_fib(5)
def fib_repeater(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib_repeater(27))