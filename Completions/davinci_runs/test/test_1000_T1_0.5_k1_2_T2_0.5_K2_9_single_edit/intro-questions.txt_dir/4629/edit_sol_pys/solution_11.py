

q = int(input())

for i in range(q):
    n = int(input())
    m = 0
    while m < n:
        m += 3**i
        print(m)
