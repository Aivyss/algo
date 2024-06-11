import sys
from itertools import combinations

heights = [int(sys.stdin.readline()) for _ in range(9)]

for c in combinations(heights, 7):
    if sum(c) == 100:
        for height in sorted(c):
            print(height)
        break
