

q = int(input())
for i in range(q):
    l1, r1, l2, r2 = [int(x) for x in input().split()]
    if r1 == l2:
        print(r1, l2)
    else:
        print(l1, l2)