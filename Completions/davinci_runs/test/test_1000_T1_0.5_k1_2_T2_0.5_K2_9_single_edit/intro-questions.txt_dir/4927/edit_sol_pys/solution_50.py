

N, P, Q = list(map(int, input().split()))

if P % (N + 1) == 0:
    print("opponent")
elif Q % (N + 1) == 0:
    print("paul")
else:
    if P // (N + 1) % 2 == 0:
        print("opponent")
    else:
        print("paul")
