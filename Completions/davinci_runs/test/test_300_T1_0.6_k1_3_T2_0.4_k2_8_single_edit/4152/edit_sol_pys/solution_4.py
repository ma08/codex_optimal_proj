n = int(input())
l = list(map(int,input().split()))

if n==1 and l[0]!=1:
    print(1)
elif n==1 and l[0]==1:
    print(0)
else:
    from collections import Counter
    c = Counter(l)
    c1 = []
    for i in range(len(c)):
        c1.append(c[i])

    print(n-max(c.values()))
