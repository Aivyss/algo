import heapq
import sys

"""
priority queue
"""
pq = []
for _ in range(int(sys.stdin.readline())):
    v = int(sys.stdin.readline())
    if v != 0:
        heapq.heappush(pq, (abs(v), v))
    else:
        print(heapq.heappop(pq)[1] if pq else 0)