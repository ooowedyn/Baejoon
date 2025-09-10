import sys

N, K = map(int, sys.stdin.readline().split())

cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
        if cnt == K:
            print(i)
            break
else:
    # for문이 break 없이 끝난 경우 (K번째 약수가 없음)
    print(0)
