

def check_bingo(bingo_card, numbers):  # bingo_card는 각 줄마다 값을 받아서 리스트로 생성 후, numbers는 숫자를 입력받아서 리스트로 생성
    bingo = False
    for i in range(3):  # bingo_card리스트의 값과 numbers리스트의 값을 비교하여 같으면 bingo를 True로 바꿔줌
        if bingo_card[i][0] in numbers and bingo_card[i][1] in numbers and bingo_card[i][2] in numbers:
            bingo = True
            break
        if bingo_card[0][i] in numbers and bingo_card[1][i] in numbers and bingo_card[2][i] in numbers:
            bingo = True
            break
    if bingo_card[0][0] in numbers and bingo_card[1][1] in numbers and bingo_card[2][2] in numbers:
        bingo = True
    if bingo_card[0][2] in numbers and bingo_card[1][1] in numbers and bingo_card[2][0] in numbers:
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
