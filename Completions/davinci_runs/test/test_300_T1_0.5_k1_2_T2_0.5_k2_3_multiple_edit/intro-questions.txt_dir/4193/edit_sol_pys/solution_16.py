

def check_bingo(bingo_card, numbers): #입력받은 빙고판과 숫자들을 비교하여 빙고가 완성되었는지 확인하는 함수
    bingo = False
    for i in range(3):
        if bingo_card[i][0] in numbers and bingo_card[i][1] in numbers and bingo_card[i][2] in numbers: #행빙고
            bingo = True
            break
        if bingo_card[0][i] in numbers and bingo_card[1][i] in numbers and bingo_card[2][i] in numbers: #열빙고
            bingo = True
            break
    if bingo_card[0][0] in numbers and bingo_card[1][1] in numbers and bingo_card[2][2] in numbers: #대각선빙고
        bingo = True
    if bingo_card[0][2] in numbers and bingo_card[1][1] in numbers and bingo_card[2][0] in numbers: #대각선빙고
        bingo = True
    return bingo #빙고가 완성되었다면 True, 아니라면 False를 리턴한다

bingo_card = [] #빙고판을 저장할 리스트
for i in range(3):
    bingo_card.append(list(map(int, input().split()))) #입력받은 빙고판을 리스트에 저장한다.
numbers = [] #추출된 숫자들을 저장할 리스트
for i in range(int(input())):
    numbers.append(int(input()))
if check_bingo(bingo_card, numbers):
    print('Yes')
else:
    print('No')
