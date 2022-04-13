n, k = [int(x) for x in input().split()]
print("n =", n)
print("k =", k)
if n == 2:
    print("YES\n")
    print("1 2")
    print("2 1")
else:
    print("YES\n")
    for i in range(1, n):
        print(i, i+1)

    print(n, 1)
