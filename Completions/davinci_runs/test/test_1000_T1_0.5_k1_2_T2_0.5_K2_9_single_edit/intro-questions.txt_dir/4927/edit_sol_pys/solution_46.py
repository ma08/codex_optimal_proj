
N, P, Q = map(int, input().split())

pauls_turn = True

while P > 0 and Q > 0:
    if pauls_turn:
        P -= N
    else:
        Q -= N
    pauls_turn = not pauls_turn

if pauls_turn:
    print("paul")
else:
    print("opponent")
