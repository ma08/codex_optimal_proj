

pieces = list(map(int, input().split())) # get the input

for i in range(6): # for each piece
    if pieces[i] == 0:
        print(1)
    elif pieces[i] == 1:
        print(1)
    elif pieces[i] == 2:
        print(2)
    elif pieces[i] == 3:
        print(2)
    elif pieces[i] == 4:
        print(2)
    elif pieces[i] == 5:
        print(8)
