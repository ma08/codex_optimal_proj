

def two_segment():
    q = int(input())
    for i in range(q):
        a, b, c, d = map(int, input().split())
        if a == b:
            print(a, c)
        elif c == d:
            print(a, c)
        else:
            print(a, c + 1)

two_segment()
