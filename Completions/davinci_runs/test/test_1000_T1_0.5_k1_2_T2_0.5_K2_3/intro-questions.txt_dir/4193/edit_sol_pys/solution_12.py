
def check_bingo(bingo_card):
    bingo = True
    for row in bingo_card:
        for number in row:
            if number == 0:
                return False
    return bingo


def check_bingo_line(bingo_card, numbers):
    bingo_line = False
    for row in bingo_card:
        if row[0] in numbers and row[1] in numbers and row[2] in numbers:
            bingo_line = True
            break
    for i in range(3):
        if bingo_card[0][i] in numbers and bingo_card[1][i] in numbers and \
                bingo_card[2][i] in numbers:
            bingo_line = True
            break
    if bingo_card[0][0] in numbers and bingo_card[1][1] in numbers and bingo_card[2][2] in numbers:
        bingo_line = True
    if bingo_card[0][2] in numbers and bingo_card[1][1] in numbers and bingo_card[2][0] in numbers:
        bingo_line = True
    return bingo_line

bingo_card = []
for i in range(3):
    bingo_card.append(list(map(int, input().split())))
numbers = []
for i in range(int(input())):
    numbers.append(int(input()))
if check_bingo(bingo_card):
    print('Yes')
elif check_bingo_line(bingo_card, numbers):
    print('Yes')
else:
    print('No')
