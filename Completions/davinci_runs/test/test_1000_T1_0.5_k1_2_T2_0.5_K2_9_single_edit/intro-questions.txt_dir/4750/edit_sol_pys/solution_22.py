
q = int(input())

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())

    if l1 == r1:
        a = l1
        b = l2
    elif l2 == r2:
        a = l1
        b = l2
    else:
        a = l1
        b = l2

    print(a, b)
