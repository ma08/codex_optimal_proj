
def check_bingo(bingo_card, nums):
    bingo_flag = False
    for i in range(len(bingo_card)):
        for j in range(len(bingo_card[i])):
            if bingo_card[i][j] in nums:
                bingo_card[i][j] = 0
    if bingo_card[0][0] == 0 and bingo_card[0][1] == 0 and bingo_card[0][2] == 0:
        bingo_flag = True  # 1
    if bingo_card[1][0] == 0 and bingo_card[1][1] == 0 and bingo_card[1][2] == 0:
        bingo_flag = True  # 2
    if bingo_card[2][0] == 0 and bingo_card[2][1] == 0 and bingo_card[2][2] == 0:
        bingo_flag = True  # 3
    if bingo_card[0][0] == 0 and bingo_card[1][0] == 0 and bingo_card[2][0] == 0:
        bingo_flag = True  # 4
    if bingo_card[0][1] == 0 and bingo_card[1][1] == 0 and bingo_card[2][1] == 0:
        bingo_flag = True  # 5
    if bingo_card[0][2] == 0 and bingo_card[1][2] == 0 and bingo_card[2][2] == 0:
        bingo_flag = True  # 6
    if bingo_card[0][0] == 0 and bingo_card[1][1] == 0 and bingo_card[2][2] == 0:
        bingo_flag = True  # 7
    if bingo_card[0][2] == 0 and bingo_card[1][1] == 0 and bingo_card[2][0] == 0:
        bingo_flag = True  # 8
    return bingo_flag

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
