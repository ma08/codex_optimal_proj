

n, x, y = map(int, input().split())
n = list(map(int, input().split()))

if n[y-1] == 0:
    n[y-1] = 1
else:
    n[y-1] = 0
    for i in range(y+1, x):
        if n[i-1] == 0:
            n[i-1] = 1
            break
        else:
            n[i-1] = 0

print(n.count(0))
