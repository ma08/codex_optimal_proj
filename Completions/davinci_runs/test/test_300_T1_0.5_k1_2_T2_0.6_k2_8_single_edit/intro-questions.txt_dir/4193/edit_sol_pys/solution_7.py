

def check_bingo(numbers, bingo_card):
    if numbers in bingo_card:
        return True

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
