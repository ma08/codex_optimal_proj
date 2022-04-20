
n, k = [int(x) for x in input().split()]

if n == 2:
    print("YES\n1 2\n2 1")
else:
    print("YES\n" + "\n".join([str(i) + " " + str(i+1) for i in range(1, n)] + [str(n) + " 1"]))
