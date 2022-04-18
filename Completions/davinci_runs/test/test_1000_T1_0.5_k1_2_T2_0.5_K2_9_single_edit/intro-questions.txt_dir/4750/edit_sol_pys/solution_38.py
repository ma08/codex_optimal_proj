

def two_segments():
    n = int(input())
    for i in range(n):
        l1, r1, l2, r2 = map(int, input().split())
        if l1 == r1:
            print(l1, r1)
        elif l2 == r2:
            print(l1, l2)
        else:
            print(l1, r2)

two_segments()
