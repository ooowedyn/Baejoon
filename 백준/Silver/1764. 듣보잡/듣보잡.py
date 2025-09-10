import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heard = {input().strip() for _ in range(N)}

common = []
for _ in range(M):
    name = input().strip()
    if name in heard:
        common.append(name)

common.sort()
print(len(common))
print('\n'.join(common))
