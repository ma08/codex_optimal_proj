

S_A = input().upper()
S_B = input().upper()
S_C = input().upper()

player = 'A'
while S_A+S_B+S_C != '' and len(S_A) > 0 and len(S_B) > 0 and len(S_C) > 0:
    if player == 'A':
        S_A, S_B, S_C = S_A[1:], S_B, S_C
        player = S_A[0]
    elif player == 'B':
        S_A, S_B, S_C = S_A, S_B[1:], S_C
        player = S_B[0]
    elif player == 'C':
        S_A, S_B, S_C = S_A, S_B, S_C[1:]
        player = S_C[0]

print(player)
