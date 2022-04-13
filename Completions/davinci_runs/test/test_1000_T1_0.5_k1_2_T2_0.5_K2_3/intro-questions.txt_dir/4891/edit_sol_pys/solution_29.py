# file

pieces = [1, 1, 2, 2, 2, 8] # how many pieces are in the puzzle
count = [int(i) for i in input().split()] # how many pieces are on the table

for i in range(6):
    print(pieces[i] - count[i], end=" ") # print the missing pieces
