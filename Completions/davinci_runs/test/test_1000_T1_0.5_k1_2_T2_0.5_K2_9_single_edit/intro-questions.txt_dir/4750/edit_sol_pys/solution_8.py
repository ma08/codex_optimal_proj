

def two_segments(l1, r1, l2, r2):
    if l1 == r1:
        print(l1, l2)
    elif l2 == r2:
        print(l1, l2)
    else:
        print(l1, l2 + 1)

q = int(input())
for i in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    two_segments(l1, r1, l2, r2)
