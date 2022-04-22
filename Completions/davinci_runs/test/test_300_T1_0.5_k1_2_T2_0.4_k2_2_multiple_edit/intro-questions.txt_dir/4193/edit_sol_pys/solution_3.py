

def check_bingo(bingo_card, number):
    bingo = False
    for i in range(3):
        if bingo_card[i][0] in number and bingo_card[i][1] in number and bingo_card[i][2] in number:
            bingo = True
            break
        if bingo_card[0][i] in number and bingo_card[1][i] in number and bingo_card[2][i] in number:
            bingo = True
            break
    if bingo_card[0][0] in number and bingo_card[1][1] in number and bingo_card[2][2] in number:
        bingo = True
    if bingo_card[0][2] in number and bingo_card[1][1] in number and bingo_card[2][0] in number:
        bingo = True
    return bingo


bingo_card = []
for i in range(3):
    bingo_card.append(list(map(int, input().split())))
number = []
for i in range(int(input())):
    number.append(int(input()))
if check_bingo(bingo_card, number):
    print('Yes')
else:
    print('No')
