import sys

s = sys.stdin.readline().strip()

i = 0
cnt = 0
while i < len(s):
    # 3글자 패턴 우선: 'dz='
    if i + 2 < len(s) and s[i:i+3] == 'dz=':
        cnt += 1
        i += 3
    # 2글자 패턴
    elif i + 1 < len(s) and s[i:i+2] in ('c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='):
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1

print(cnt)
