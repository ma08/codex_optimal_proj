

def check_bingo(bingo_card, numbers):
    bingo = False
    for i in range(len(bingo_card)):
        if bingo:
            break;
        for j in range(len(bingo_card[0])):
            if bingo:
                break;
            if bingo_card[i][j] in numbers:
                bingo = True
                for k in range(len(bingo_card)):
                    if bingo_card[k][j] not in numbers:
                        bingo = False
                        break;
                    if bingo_card[i][k] not in numbers:
                        bingo = False
                        break;
                if bingo:
                    break;
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
