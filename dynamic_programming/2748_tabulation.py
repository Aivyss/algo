import sys

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


n = int(sys.stdin.readline())
print(fibonacci(n))