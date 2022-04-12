

N, P, Q = map(int, input().split())  # N is the number of stones, P is the number of stones Paul has, Q is the number of stones the opponent has.

pauls_turn = True  # Paul starts first.

while P + Q > 0:
    if pauls_turn:
        P -= N
    else:
        Q -= N
    pauls_turn = not pauls_turn

if pauls_turn:
    print("paul")
else:
    print("opponent")
