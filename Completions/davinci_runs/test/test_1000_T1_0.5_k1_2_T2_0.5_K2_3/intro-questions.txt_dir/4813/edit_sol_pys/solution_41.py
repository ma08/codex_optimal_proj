

word = "HANGMAN"  # input()
perm = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # input()


letters = dict()
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    letters[i] = 0

for i in word:
    letters[i] += 1

for i in perm:
    if letters[i] > 0:
        letters[i] -= 1
    else:
        print("LOSE")
        break
else:
    print("WIN")
