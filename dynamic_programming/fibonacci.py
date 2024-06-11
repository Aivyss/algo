"""
top-down
dp table
"""
cache = dict()


def fibonacci(n):
    if n == 0 or n == 1:
        return n

    v = cache.get(n)
    if v:
        return v

    a = fibonacci(n - 1)
    cache[n - 1] = a
    b = fibonacci(n - 2)
    cache[n - 2] = b

    return a + b


print(fibonacci(6))
