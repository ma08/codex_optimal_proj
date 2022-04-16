

N, P, Q = [int(x) for x in input().split()]  # input()

if P % (N + 1) == 0:
    print("opponent")  # print()
elif Q % (N + 1) == 0:
    print("paul")  # print()
else:
    if P // (N + 1) % 2 == 0:
        print("opponent")  # print()
    else:
        print("paul")  # print()
