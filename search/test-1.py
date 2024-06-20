import sys


def dfs(graph, i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False

    if graph[i][j] == '0':
        graph[i][j] = '1'
        dfs(graph, i - 1, j)
        dfs(graph, i + 1, j)
        dfs(graph, i, j - 1)
        dfs(graph, i, j + 1)
        return True

    return False


n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(graph, i, j):
            cnt += 1

print(cnt)
