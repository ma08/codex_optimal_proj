
N, P, Q = map(int, input().split())

pauls_turn = True

while P + Q > 0:
    if pauls_turn:
        if P >= N:
            P -= N
    else:
        if Q >= N:
            Q -= N
    pauls_turn = not pauls_turn

if pauls_turn:
    print("paula")
else:
    print("opponent")
