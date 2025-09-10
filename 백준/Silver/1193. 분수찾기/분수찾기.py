import sys

X = int(sys.stdin.readline())

# X가 포함된 대각선 번호 n과 그 대각선의 누적 끝값 total을 구함
n = 1
total = 1
while X > total:
    n += 1
    total += n

prev_total = total - n
k = X - prev_total  # 해당 대각선에서의 1-based 위치

# 대각선 번호의 홀짝에 따라 순서가 반대
if n % 2 == 1:      # 홀수 대각선: 위에서 아래로 (n/1 -> ... -> 1/n)
    num = n - k + 1
    den = k
else:               # 짝수 대각선: 아래에서 위로 (1/n -> ... -> n/1)
    num = k
    den = n - k + 1

print(f"{num}/{den}")
