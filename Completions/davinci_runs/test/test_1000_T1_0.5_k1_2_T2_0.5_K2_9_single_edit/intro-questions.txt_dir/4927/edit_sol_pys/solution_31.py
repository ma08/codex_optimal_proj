
N = int(input())
P = int(input())
Q = int(input())

pauls_turn = True

while P + Q > 0:
    if pauls_turn:
        P -= 1
    else:
        Q -= 1
    pauls_turn = not pauls_turn

if pauls_turn:
    print("paul")
else:
    print("opponent")
