
#
# Solution

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    if len(set(l)) == 1:
        print('YES')
    elif len(set(l)) == 2:
        print('YES')
    else:
        print('NO')
