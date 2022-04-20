

n = int(input())

dice_list = []

for i in range(n):
    dice_list.append(list(map(int, input().split())))
if n > 1:
    for i in range(n-2):
        if dice_list[i][0] == dice_list[i][1] and dice_list[i+1][0] == dice_list[i+1][1] and dice_list[i+2][0] == dice_list[i+2][1]:
            print("Yes")
            exit()

print("No")
