
q = int(input())

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())

    a = l1
    b = l2
    if l1 == l2:
        b = r2

    print(a, b)
