

def check_bingo(bingo_card, numbers):
    bingo = False
    for i in range(5):
        if not bingo:
            for j in range(5):
                if bingo_card[i][j] in numbers:
                    bingo_card[i][j] = 0
            if bingo_card[i][0] == 0 and bingo_card[i][1] == 0 and bingo_card[i][2] == 0 and bingo_card[i][3] == 0 and bingo_card[i][4] == 0:
                bingo = True
                break
        if not bingo:
            for j in range(5):
                if bingo_card[j][i] in numbers:
                    bingo_card[j][i] = 0
            if bingo_card[0][i] == 0 and bingo_card[1][i] == 0 and bingo_card[2][i] == 0 and bingo_card[3][i] == 0 and bingo_card[4][i] == 0:
                bingo = True
                break
    if not bingo:
        for i in range(5):
            if bingo_card[i][i] in numbers:
                bingo_card[i][i] = 0
        if bingo_card[0][0] == 0 and bingo_card[1][1] == 0 and bingo_card[2][2] == 0 and bingo_card[3][3] == 0 and bingo_card[4][4] == 0:
            bingo = True
    if not bingo:
        for i in range(5):
            if bingo_card[i][4-i] in numbers:
                bingo_card[i][4-i] = 0
        if bingo_card[0][4] == 0 and bingo_card[1][3] == 0 and bingo_card[2][2] == 0 and bingo_card[3][1] == 0 and bingo_card[4][0] == 0:
            bingo = True
    return bingo

bingo_card = []
for i in range(5):
    bingo_card.append(list(map(int, input().split())))
numbers = []
for i in range(int(input())):
    numbers.append(int(input()))
if check_bingo(bingo_card, numbers):
    print('Yes')
else:
    print('No')
