

pieces = list(map(int, input().split())) # get the input

for i in range(6): # for each piece
    print(8 - pieces[i], end=' ')
