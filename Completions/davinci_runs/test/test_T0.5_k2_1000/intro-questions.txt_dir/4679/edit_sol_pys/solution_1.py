
S_A = input().strip()
S_B = input().strip()
S_C = input().strip()

player = 'A'
while S_A+S_B+S_C != '' and S_A+S_B+S_C != '   ' and S_A+S_B+S_C != '  ':
    if player == 'A':
        S_A, S_B, S_C = S_A[1:], S_B, S_C
        player = S_A[0]
        if player == '' or player == ' ':
            player = 'A'
            break
    elif player == 'B':
        S_A, S_B, S_C = S_A, S_B[1:], S_C
        player = S_B[0]
        if player == '' or player == ' ':
            player = 'B'
            break
    elif player == 'C':
        S_A, S_B, S_C = S_A, S_B, S_C[1:]
        player = S_C[0]
        if player == '' or player == ' ':
            player = 'C'
            break

print(player)
