N, P, Q = [int(x) for x in input().split()]

print("opponent" if P % (N + 1) == 0 or Q % (N + 1) == 0 or P // (N + 1) % 2 == 0 else "paul")
