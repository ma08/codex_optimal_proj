

n = int(input())
words = []
for i in range(n):
    words.append(input())

player = 2
for i in range(n - 1):
    if words[i][-1] != words[i + 1][0] or words[i + 1] == words[i + 2]:
        print("Player {} lost".format(player))
        exit()
    player = (player % 2) + 1
else:
    print("Fair Game")
