import sys
sys.setrecursionlimit(10**6)

S_A = input() # スタックA
S_B = input() # スタックB
S_C = input() # スタックC

player = 'A'
while S_A+S_B+S_C != '' or player == '':
    if player == 'A':
        S_A, S_B, S_C = S_A[1:], S_B, S_C
        player = S_A[0]
        if player == '':
            player = 'A'
            break
    elif player == 'B':
        S_A, S_B, S_C = S_A, S_B[1:], S_C
        player = S_B[0]
        if player == '':
            player = 'B'
            break
    elif player == 'C':
        S_A, S_B, S_C = S_A, S_B, S_C[1:]
        player = S_C[0]
        if player == '':
            player = 'C'
            break

print(player)
