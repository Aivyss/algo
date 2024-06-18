from collections import deque


def dfs(graph, v, visited):
    """
    DFS (Depth-First Search)
    # 개요
    이름 그대로 깊이 우선 탐색. 깊은 부분을 우선적으로 탐색하는 알고리즘

    스택 자료구조나 재귀함수를 이용한다.

    1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다.
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
    """
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    """
    BFS(Breadth-First Search)

    # 개요
    너비우선 탐색이라고 불림 가까운 노드부터 우선적으로 탐색하는 알고리즘

    큐 자료구조를 이용한다.

    1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.
    3. 2를 수행할 수 없을 때까지 반복한다.

    ## 특징
    - 노드의 최단거리 순으로 탐색한다.
    """
    q = deque([v])
    visited[v] = True

    while q:
        v = q.popleft()
        print(v, end=' ')

        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True


graph = [
    [],  # ignore
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

dfs(graph, 1, [False]*9)
print()
bfs(graph, 1, [False]*9)
