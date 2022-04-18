from collections import defaultdict

n, k = map(int, input().split())

a = list(map(int, input().split()))
if n == 1:
    print("YES\n1")
else:
    b = [0] * n
    for i in range(n):
        if a[i] == a[0]:
            b[i] = 1
        else:
            b[i] = 2
    if a[0] in a[1:] or k != 2:
        print("NO\n")
    else:
        print("YES\n" + " ".join(map(str, b)))
