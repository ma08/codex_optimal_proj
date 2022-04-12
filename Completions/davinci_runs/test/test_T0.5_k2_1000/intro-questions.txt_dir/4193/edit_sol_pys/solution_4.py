
def check_bingo(bingo_card, numbers): #check if bingo
    bingo = False #init
    for i in range(3):
        if bingo_card[i][0] in numbers and bingo_card[i][1] in numbers and bingo_card[i][2] in numbers: #check rows
            bingo = True
            break
        if bingo_card[0][i] in numbers and bingo_card[1][i] in numbers and bingo_card[2][i] in numbers: #check columns
            bingo = True
            break
    if bingo_card[0][0] in numbers and bingo_card[1][1] in numbers and bingo_card[2][2] in numbers: #check diagonal
        bingo = True
    if bingo_card[0][2] in numbers and bingo_card[1][1] in numbers and bingo_card[2][0] in numbers: #check diagonal
        bingo = True
    return bingo

bingo_card = []
for i in range(3):
    bingo_card.append(list(map(int, input().split())))
numbers = []
for i in range(int(input())):
    numbers.append(int(input()))
if check_bingo(bingo_card, numbers):
    print('Yes')
else:
    print('No')
