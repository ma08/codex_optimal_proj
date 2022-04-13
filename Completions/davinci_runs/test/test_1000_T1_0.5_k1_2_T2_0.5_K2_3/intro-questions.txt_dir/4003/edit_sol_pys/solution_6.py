

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R")
else:
    l = []
    r = []
    for i in range(n):
        if i == 0 or a[i] > l[-1]:
            l.append(a[i])
    for i in range(n-1, -1, -1):
        if i == n-1 or a[i] > r[-1]:
            r.append(a[i])
    print(max(len(l), len(r)))
    print("L"*len(l) if len(l) > len(r) else "R"*len(r))
