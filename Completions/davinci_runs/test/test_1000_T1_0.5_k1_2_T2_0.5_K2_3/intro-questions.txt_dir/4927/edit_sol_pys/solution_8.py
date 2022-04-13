N, P, Q = map(int, input().split())
Pauls_turn = True

while P + Q > 0:
    if Pauls_turn:
        P -= N if P >= N else P
    else:
        Q -= N if Q >= N else Q
    Pauls_turn = not Pauls_turn

if Pauls_turn:
    print("paul")
else:
    print("opponent")
