import sys

n = int(input())
a = list(map(int, input().split()))

def check(a):
    if len(a) == 1:
        return True
    if len(a) == 2:
        return a[0] == a[1] // 2 or a[0] == a[1] * 3
    if a[0] == a[1] // 2:
        return check(a[1:])
    if a[0] == a[1] * 3:
        return check(a[1:])
    return False

for i in range(n):
    if check(a[i:]):
        sys.stdout.write(' '.join(map(str, a[i:])))
        break
