fib_cache = {}

def fibonacci(n):
    if n == 0 or n == 1:
        fib_cache[n] = n
        return n
    elif n in fib_cache:
        return fib_cache[n]
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        fib_cache[n] = result
        return result


n = int(input())
print(fibonacci(n))
