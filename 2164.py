from collections import deque

"""
queue
"""

n = int(input())
q = deque(range(1, n + 1))

while len(q) > 1:
    q.popleft()
    num_move_to_behind = q.popleft()
    q.append(num_move_to_behind)

print(q.popleft())
