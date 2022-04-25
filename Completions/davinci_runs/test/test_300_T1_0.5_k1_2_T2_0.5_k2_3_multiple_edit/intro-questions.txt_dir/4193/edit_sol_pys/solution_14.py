

def check_bingo(bingo_card, numbers, bingo):
    if bingo_card[0][0] in numbers and bingo_card[0][1] in numbers and bingo_card[0][2] in numbers:
        bingo = True
    if bingo_card[1][0] in numbers and bingo_card[1][1] in numbers and bingo_card[1][2] in numbers:
        bingo = True
    if bingo_card[2][0] in numbers and bingo_card[2][1] in numbers and bingo_card[2][2] in numbers:
        bingo = True
    if bingo_card[0][0] in numbers and bingo_card[1][0] in numbers and bingo_card[2][0] in numbers:
        bingo = True
    if bingo_card[0][1] in numbers and bingo_card[1][1] in numbers and bingo_card[2][1] in numbers:
        bingo = True
    if bingo_card[0][2] in numbers and bingo_card[1][2] in numbers and bingo_card[2][2] in numbers:
        bingo = True
    if bingo_card[0][0] in numbers and bingo_card[1][1] in numbers and bingo_card[2][2] in numbers:
        bingo = True
    if bingo_card[0][2] in numbers and bingo_card[1][1] in numbers and bingo_card[2][0] in numbers:
        bingo = True

bingo_card = []
for i in range(3):
    bingo_card.append(list(map(int, input().split())))
numbers = []
for i in range(int(input())):
    numbers.append(int(input()))
bingo = False
check_bingo(bingo_card, numbers, bingo)
if bingo:
    print('yes')
else:
    print('no')
