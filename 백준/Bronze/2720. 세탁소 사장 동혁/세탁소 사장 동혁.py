import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    c = int(input())  # 거스름돈(센트)
    q = c // 25
    c %= 25
    d = c // 10
    c %= 10
    n = c // 5
    c %= 5
    p = c
    print(q, d, n, p)
