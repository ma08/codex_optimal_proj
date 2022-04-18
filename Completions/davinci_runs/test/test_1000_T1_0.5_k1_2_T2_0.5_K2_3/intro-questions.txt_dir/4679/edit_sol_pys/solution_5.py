

S_A = input()
S_B = input()
S_C = input()

player = 'A'
while S_A + S_B + S_C != '':  # Continue as long as there are still cards in the pile
    if player == 'A':
        S_A, S_B, S_C = S_A[1:], S_B, S_C  # The first card is removed
        player = S_A[0]
        if player == '':  # If the pile is empty, the player wins
            player = 'A'
            break
    elif player == 'B':
        S_A, S_B, S_C = S_A, S_B[1:], S_C  # The first card is removed
        player = S_B[0]
        if player == '':  # If the pile is empty, the player wins
            player = 'B'
            break
    elif player == 'C':
        S_A, S_B, S_C = S_A, S_B, S_C[1:]  # The first card is removed
        player = S_C[0]
        if player == '':  # If the pile is empty, the player wins
            player = 'C'
            break

print(player)
