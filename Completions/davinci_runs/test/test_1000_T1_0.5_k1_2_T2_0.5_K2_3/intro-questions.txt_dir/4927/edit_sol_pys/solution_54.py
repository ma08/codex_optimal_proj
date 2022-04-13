
N, P, Q = map(int, input().split())

Pauls_turn = True

while P + Q > 0:
    if Pauls_turn:
        if P - N >= 0:
            P -= N
        else:
            P = 0
    else:
        if Q - N >= 0:
            Q -= N
        else:
            Q = 0
    Pauls_turn = not Pauls_turn

if Pauls_turn:
    print("paul")
else:
    print("opponent")
