from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
c = Counter(a)
if len(c) == 1:
    print("YES")
    print(1)
else:
    b = [0]*n
    for i in range(n):
        if a[i] == a[0]:
            b[i] = 1
        else:
            b[i] = 2
    if c[a[0]] > 1:
        print("NO")
    else:
        print("YES")
        print(*b)
