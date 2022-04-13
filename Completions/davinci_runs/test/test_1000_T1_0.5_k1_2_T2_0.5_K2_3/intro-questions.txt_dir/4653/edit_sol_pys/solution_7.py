t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 1:
        print(n)
        continue
    if k >= 3:
        if n//k >= 1:
            print(n//k)
            continue
        if n//k == 0:
            print(1)
            continue
