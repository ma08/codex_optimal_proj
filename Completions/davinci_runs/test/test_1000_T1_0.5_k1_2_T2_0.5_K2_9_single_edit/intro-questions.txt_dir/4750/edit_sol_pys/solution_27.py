

def two_segments():
    q = int(input())
    for i in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == y1:
            print(x1, x2)
        elif x2 == y2:
            print(x1, x2)
        else:
            print(x1, x2 + 1)

two_segments()
