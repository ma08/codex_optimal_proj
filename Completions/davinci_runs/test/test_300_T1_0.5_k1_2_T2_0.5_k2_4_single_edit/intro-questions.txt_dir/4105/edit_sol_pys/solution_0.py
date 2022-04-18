
n, k = [int(x) for x in input().split()]

if n == 2:
    print("1 2")
    print("2 1")
else:
    for i in range(1, n):
        print(i, i+1)
    print(n, 1)
