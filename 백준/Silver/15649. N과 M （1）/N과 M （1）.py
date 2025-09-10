import sys
input = sys.stdin.readline

N, M = map(int, input().split())

used = [False] * (N + 1)
path = [0] * M
out = []

def dfs(depth: int):
    if depth == M:
        out.append(' '.join(map(str, path)))
        return
    for num in range(1, N + 1):  # 1부터 순회하여 사전순 보장
        if not used[num]:
            used[num] = True
            path[depth] = num
            dfs(depth + 1)
            used[num] = False

dfs(0)
print('\n'.join(out))
