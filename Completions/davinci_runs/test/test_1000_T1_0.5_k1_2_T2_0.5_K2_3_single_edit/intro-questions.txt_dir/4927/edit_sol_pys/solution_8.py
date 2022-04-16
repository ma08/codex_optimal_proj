

n, p, q = [int(x) for x in input().split()]

if p % (n + 1) == 0:
    print("opponent")
elif q % (n + 1) == 0:
    print("paul")
else:
    if p // (n + 1) % 2 == 0:
        print("opponent")
    else:
        print("paul")
