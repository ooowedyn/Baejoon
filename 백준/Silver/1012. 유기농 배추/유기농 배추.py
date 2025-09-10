import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
answers = []

# 상, 하, 좌, 우
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(T):
    M, N, K = map(int, input().split())  # M: 가로(열), N: 세로(행)
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1  # 좌표는 (열=x, 행=y)

    worms = 0
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1 and not visited[r][c]:
                worms += 1
                # BFS로 연결된 배추들을 모두 방문 처리
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in DIRS:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < N and 0 <= nc < M:
                            if field[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
    answers.append(str(worms))

print("\n".join(answers))