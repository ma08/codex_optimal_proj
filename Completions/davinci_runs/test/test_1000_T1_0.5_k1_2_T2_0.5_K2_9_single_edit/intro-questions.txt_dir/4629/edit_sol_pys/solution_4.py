

q = int(input())

for i in range(q):
    n = int(input())
    x = 0
    while x < n:
        x += 3**i
    print(x)
