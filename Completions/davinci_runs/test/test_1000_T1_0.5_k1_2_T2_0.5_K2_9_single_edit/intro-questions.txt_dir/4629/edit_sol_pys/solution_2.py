

q = int(input())

for i in range(q):
    n = int(input())
    if n == 1:
        print(0)
    else:
        m = 0
        while m < n:
            m += 3**i
        print(m)
