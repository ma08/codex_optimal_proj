

n, r = [int(x) for x in input().split()]

for i in range(n):
    a, b = [int(x) for x in input().split()]
    if a > r:
        print("NO")
        exit()
    r += b

if r >= 0:
    print("YES")
else:
    print("NO")