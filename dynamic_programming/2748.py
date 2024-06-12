import sys

cache = {
    0: 0,
    1: 1,
}
def fibonacci(n):
    v = cache.get(n)
    if v is None:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache.get(n)


n = int(sys.stdin.readline())
print(fibonacci(n))