
pieces = [1, 1, 2, 2, 2, 8]  # all pieces in the chess
count = [int(i) for i in input().split()]

for i in range(6):  # print the missing pieces
    print(pieces[i] - count[i], end=" ")
