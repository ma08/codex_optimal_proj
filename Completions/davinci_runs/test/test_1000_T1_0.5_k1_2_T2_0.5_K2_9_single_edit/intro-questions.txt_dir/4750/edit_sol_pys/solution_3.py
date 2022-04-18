

def two_segments():
    q = int(input())
    for i in range(q):
        l1, r1 = map(int, input().split())
        l2, r2 = map(int, input().split())
        print(l1, r2)

two_segments()
