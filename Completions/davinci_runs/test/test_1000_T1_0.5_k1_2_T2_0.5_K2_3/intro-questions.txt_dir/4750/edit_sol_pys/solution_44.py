q = int(input())

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())

    if l1 == r1 or l2 == r2:
        a = l1
        b = l2
    elif l1 == l2 or r1 == r2 or l1 == r2 or r1 == l2:
        a = l1
        b = r2
    else:
        a = l1
        b = l2

    print(a, b)
