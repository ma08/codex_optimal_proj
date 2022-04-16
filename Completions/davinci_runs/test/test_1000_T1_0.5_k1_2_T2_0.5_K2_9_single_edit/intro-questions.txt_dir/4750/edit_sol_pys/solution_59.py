
def two_segments(q):
    for i in range(int(q)):
        l1, r1, l2, r2 = map(int, q.split())
        if l1 == r1: print(l1, l2)
        elif l2 == r2: print(l1, l2)
        else: print(l1, l2 + 1)
