# this is a comment

q = int(input())

for i in range(q):
    n = int(input())
    a = 0
    while a < n:
        a += 3**i
    print(a)
