
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] > 0:
        print("NO")
    else:
        print("YES")
