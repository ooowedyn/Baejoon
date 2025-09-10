'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 간선 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점의 인접 리스트 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS (재귀)
visited_dfs = [False] * (N + 1)
dfs_result = []

def dfs(v):
    visited_dfs[v] = True
    dfs_result.append(v)
    for nxt in graph[v]:
        if not visited_dfs[nxt]:
            dfs(nxt)

# BFS
visited_bfs = [False] * (N + 1)
bfs_result = []

def bfs(start):
    q = deque([start])
    visited_bfs[start] = True
    while q:
        v = q.popleft()
        bfs_result.append(v)
        for nxt in graph[v]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                q.append(nxt)

# 실행
dfs(V)
bfs(V)

# 출력
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))