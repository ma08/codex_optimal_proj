

def two_segments():
    q = int(input())
    for i in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        if l1 == r1:
            print(l1, l2)
        elif l2 == r2:
            print(l1, l2)
        else:
            print(l1, l2 + 1)

two_segments()
