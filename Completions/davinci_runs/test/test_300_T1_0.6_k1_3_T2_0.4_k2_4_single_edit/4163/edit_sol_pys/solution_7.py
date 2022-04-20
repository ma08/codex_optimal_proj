

n = int(input())
doublets = []

for i in range(n):
    dice1, dice2 = map(int, input().split())  # map(int, input().split())
    doublets.append(dice1 == dice2)

for i in range(len(doublets) - 2):  # len(doublets) - 2
    if doublets[i] and doublets[i + 1] and doublets[i + 2]:
        print("Yes")
        exit()

print("No")
