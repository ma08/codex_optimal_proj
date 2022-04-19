

n, k = map(int, input().split())

a = list(map(int, input().split()))

a.sort()
print(a)
moves = 0

if k == n:
    print(a[-1] - a[0])
else:
    while a[-1] - a[0] != 0:
        a[-1] -= 1
        a[0] += 1
        moves += 1
        print(a)
        a.sort()
    print(moves)
