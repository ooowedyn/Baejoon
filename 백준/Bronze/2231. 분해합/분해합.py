import sys

N = int(sys.stdin.readline().strip())

start = max(1, N - 9 * len(str(N)))
answer = 0

for m in range(start, N):
    if m + sum(map(int, str(m))) == N:
        answer = m
        break

print(answer)
