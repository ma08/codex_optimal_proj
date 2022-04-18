
n = int(input())
words = []
for i in range(n):
    words.append(input().lower())

player = 1
for i in range(n - 1):
    if words[i][-1] != words[i + 1][0] or i < n - 2 and words[i + 1] == words[i + 2]:
        print("Player {} lost".format(player))
        exit()
    player = (player % 2) + 1
else:
    print("Fair Game")
