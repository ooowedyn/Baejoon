import sys

N = int(sys.stdin.readline())

answer = -1
for five in range(N // 5, -1, -1):   # 5kg 봉지 개수를 최대로부터 줄여가며 확인
    rem = N - 5 * five
    if rem % 3 == 0:                 # 남은 무게가 3으로 나누어떨어지면 가능
        answer = five + (rem // 3)
        break

print(answer)