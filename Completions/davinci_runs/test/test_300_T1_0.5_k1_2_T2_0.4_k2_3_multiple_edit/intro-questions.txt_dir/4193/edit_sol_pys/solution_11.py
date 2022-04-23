
def check_bingo(bingo_card, bingo_numbers):
    bingo_check = False
    for i in range(3):
        if bingo_card[i][0] in bingo_numbers and bingo_card[i][1] in bingo_numbers and bingo_card[i][2] in bingo_numbers:
            bingo_check = True
            break
        if bingo_card[0][i] in bingo_numbers and bingo_card[1][i] in bingo_numbers and bingo_card[2][i] in bingo_numbers:
            bingo_check = True
            break
    if bingo_card[0][0] in bingo_numbers and bingo_card[1][1] in bingo_numbers and bingo_card[2][2] in bingo_numbers:
        bingo_check = True
    if bingo_card[0][2] in bingo_numbers and bingo_card[1][1] in bingo_numbers and bingo_card[2][0] in bingo_numbers:
        bingo_check = True
    return bingo_check

bingo_card = []
for i in range(3):
    bingo_card.append(list(map(int, input().split())))
bingo_numbers = []
for i in range(int(input())):
    bingo_numbers.append(int(input()))
if check_bingo(bingo_card, bingo_numbers):
    print('Yes')
else:
    print('No')
