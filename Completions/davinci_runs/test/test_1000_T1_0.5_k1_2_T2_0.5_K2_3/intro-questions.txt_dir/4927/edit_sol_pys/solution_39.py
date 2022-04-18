

N, P, Q = [int(x) for x in input().split()]  # get the number of rounds and the number of points for both players

if P % (N + 1) == 0:  # if the number of points for the opponent is a multiple of the number of rounds + 1, the opponent wins
    print("opponent")
elif Q % (N + 1) == 0:
    print("paul")
else:
    if P // (N + 1) % 2 == 0:
        print("opponent")
    else:
        print("paul")
