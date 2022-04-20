
def check_bingo(bingo_card, numbers):
    bingo = True
    for i in range(3):
        if bingo_card[i][0] not in numbers or bingo_card[i][1] not in numbers or bingo_card[i][2] not in numbers:
            bingo = False
            break
        if bingo_card[0][i] not in numbers or bingo_card[1][i] not in numbers or bingo_card[2][i] not in numbers:
            bingo = False
            break
    if bingo_card[0][0] not in numbers or bingo_card[1][1] not in numbers or bingo_card[2][2] not in numbers:
        bingo = False
    if bingo_card[0][2] not in numbers or bingo_card[1][1] not in numbers or bingo_card[2][0] not in numbers:
        bingo = False
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
