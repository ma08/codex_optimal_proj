

import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))  # 타입 캐스팅

a.sort(reverse=True)  # 역순 정렬

b = []

for i in range(n):
    b.append(a.pop(0))
    if a and a[0]*2 == b[-1]:
        b.append(a.pop(0))

print(' '.join(map(str, b)))
