

q = int(input())
for i in range(q):
    a, b, c, d = [int(x) for x in input().split()]
    if b == c:
        print(b, c)
    else:
        print(a, c)
