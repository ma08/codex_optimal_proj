
q = int(input())

for i in range(q):
    n,k,b = map(int, input().split())
    if k > 0:
        if b == 1:
            print(n-1, 1)
        else:
            print(1, n-1)
    else:
        print(1, n-1)
