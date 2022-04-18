

word = input()
letters = input()

# create a dictionary of letters and their positions
letter_dict = {}
for i in range(len(word)):
    if word[i] in letter_dict:
        letter_dict[word[i]].append(i)
    else:
        letter_dict[word[i]] = [i + 1]

# check if Ned wins
win = True
for letter in letters:
    if letter in letter_dict:
        del letter_dict[letter]
        if not letter_dict:
            break
    else:
        win = False
        break

# print output
if win:
    print("WIN")
else:
    print("LOSE")
