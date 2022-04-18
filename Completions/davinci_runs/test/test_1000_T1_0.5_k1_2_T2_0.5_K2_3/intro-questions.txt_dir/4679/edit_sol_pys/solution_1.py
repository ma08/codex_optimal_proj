

S_A = list(input()) # スタックA
S_B = list(input()) # スタックB
S_C = list(input()) # スタックC

player = 'A'
while len(S_A)+len(S_B)+len(S_C) != 0:
    if player == 'A':
        S_A, S_B, S_C = S_A[1:], S_B, S_C
        player = S_A[0]
        if len(S_A) == 0:
            player = 'A'
            break
    elif player == 'B':
        S_A, S_B, S_C = S_A, S_B[1:], S_C
        player = S_B[0]
        if len(S_B) == 0:
            player = 'B'
            break
    elif player == 'C':
        S_A, S_B, S_C = S_A, S_B, S_C[1:]
        player = S_C[0]
        if len(S_C) == 0:
            player = 'C'
            break

print(player)
