q = int(input())

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())

    a = l1
    b = l2
    if l1 == r1 and l2 == r2:
        if l1 == l2:
            a = l1
            b = r2
        else:
            a = l1
            b = l2
    elif l1 == r1:
        if l1 == l2:
            a = l1
            b = r2
        elif l1 == r2:
            a = l1
            b = l2
    elif l2 == r2:
        if l2 == l1:
            a = l1
            b = r2
        elif l2 == r1:
            a = l1
            b = r2

    print(a, b)
