
n = int(input())
doublets = []

for i in range(n):
    dice_1, dice_2 = map(int, input().split())
    doublets.append(dice_1 == dice_2)

for i in range(len(doublets) - 2):
    if doublets[i] and doublets[i+1] and doublets[i+2]:
        print("Yes")
        exit()

print("No")
