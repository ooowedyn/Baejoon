import sys

s = sys.stdin.readline().strip()

groups = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0
for ch in s:
    for i, g in enumerate(groups):
        if ch in g:
            time += i + 3
            break

print(time)