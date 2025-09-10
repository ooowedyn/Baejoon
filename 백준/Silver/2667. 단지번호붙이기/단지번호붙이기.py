import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
sizes = []

for r in range(N):
    for c in range(N):
        if grid[r][c] == 1 and not visited[r][c]:
            visited[r][c] = True
            q = deque([(r, c)])
            cnt = 1
            while q:
                cr, cc = q.popleft()
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                            cnt += 1
            sizes.append(cnt)

sizes.sort()
print(len(sizes))
print("\n".join(map(str, sizes)))
