

# Solved

import sys

n = int(input())
a = list(map(int, input().split()))

max_a = max(a)
min_a = min(a)

if n == 1:
    print(0)
    sys.exit()

if max_a == min_a:
    print(0)
    sys.exit()

if max_a - min_a > 100:
    print(-1)
    sys.exit()

for i in range(max_a - min_a + 1):
    if i == 0:
        continue

    flag = True

    for j in range(len(a)):
        if a[j] - i < min_a:
            flag = False
            break

    if flag:
        print(i)
        sys.exit()

print(-1)