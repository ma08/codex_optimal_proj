

def check_bingo(bingo_card, number):
    for i in range(5):
        for j in range(5):
            if bingo_card[i][j] == number:
                bingo_card[i][j] = 0
    return bingo_card

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
