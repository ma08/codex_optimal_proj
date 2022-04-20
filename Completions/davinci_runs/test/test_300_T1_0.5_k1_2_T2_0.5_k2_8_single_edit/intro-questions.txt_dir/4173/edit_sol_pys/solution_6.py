
t = int(input())
for i in range(t):
    n = int(input())
    x = [int(x) for x in input().split()]
    d = dict()
    for j in range(n):
        d[x[j]] = j+1
    d = sorted(d.items(), key=lambda x: x[1])
    print(d)
    print(d[0][0], d[-1][0])
