

N = int(input())
a = list(map(int, input().split()))[:N]
b = [0]*N
for i in range(N):
    if a[i] == a[0]:
        b[i] = 1
    else:
        b[i] = 2
if a[0] in a[1:]:
    print("NO")
else:
    print("YES")
    print(*b)
