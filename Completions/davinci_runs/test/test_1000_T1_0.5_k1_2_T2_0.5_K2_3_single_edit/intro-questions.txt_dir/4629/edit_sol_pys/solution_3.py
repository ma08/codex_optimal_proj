
q = int(input())

for i in range(q):
    n = int(input())
    x = 0
    for j in range(n):
        x += 3**j
    print(x)
