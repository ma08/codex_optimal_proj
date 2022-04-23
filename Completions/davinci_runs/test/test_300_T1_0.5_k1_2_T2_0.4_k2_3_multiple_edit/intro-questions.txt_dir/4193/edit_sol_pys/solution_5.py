

def check_bingo(bingo_card, nums):
    bingo_flag = False
    for i in range(3):
        if bingo_card[i][0] in nums and bingo_card[i][1] in nums and bingo_card[i][2] in nums:
            bingo_flag = True
            break
        if bingo_card[0][i] in nums and bingo_card[1][i] in nums and bingo_card[2][i] in nums:
            bingo_flag = True
            break
    if bingo_card[0][0] in nums and bingo_card[1][1] in nums and bingo_card[2][2] in nums:
        bingo_flag = True
    if bingo_card[0][2] in nums and bingo_card[1][1] in nums and bingo_card[2][0] in nums:
        bingo_flag = True
    return bingo_flag

bingo_card = []
for i in range(3):
    bingo_card.append(list(map(int, input().split()))
nums = []
for i in range(int(input())):
    nums.append(int(input()))
if check_bingo(bingo_card, nums):
    print('Yes')
else:
    print('No')
