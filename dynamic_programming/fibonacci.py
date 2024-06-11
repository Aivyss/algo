"""
top-down
dp table
"""

cache = dict()


def top_down_fibonacci(n):
    if n == 0 or n == 1:
        return n

    v = cache.get(n)
    if v:
        return v

    a = top_down_fibonacci(n - 1)
    cache[n - 1] = a
    b = top_down_fibonacci(n - 2)
    cache[n - 2] = b

    return a + b


print(top_down_fibonacci(6))

"""
bottom-up
"""


def bottom_up_fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a
