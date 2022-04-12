N = int(input())
words = []

for i in range(N):
    words.append(input())
for i in range(1, N):
    if words[i][0] != words[i - 1][-1]:
        print("Player " + str(i % 2 + 1) + " lost")
        exit()

print("Fair Game")
