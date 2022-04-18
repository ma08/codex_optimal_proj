
n, m, d = map(int, input().split())
c = list(map(int, input().split()))
if d == 1:
    print("YES")
    for i in range(n):
        print(i % m + 1, end=" ")
else:
    print("NO")
