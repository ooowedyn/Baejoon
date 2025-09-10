import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

# 방문 겸 거리 배열 (시작 칸을 1로)
dist = [[0]*M for _ in range(N)]
dist[0][0] = 1

q = deque([(0, 0)])
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    r, c = q.popleft()
    if r == N-1 and c == M-1:   # 도착 시 조기 종료 가능
        break
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if grid[nr][nc] == 1 and dist[nr][nc] == 0:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

print(dist[N-1][M-1])