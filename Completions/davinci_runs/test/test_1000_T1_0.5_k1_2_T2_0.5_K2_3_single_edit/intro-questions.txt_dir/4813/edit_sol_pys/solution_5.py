

word = input("Enter word: ")
letters = input("Enter letters: ")

# create a dictionary of letters and their positions
letter_dict = {}
for i in range(len(word)):
    if word[i] in letter_dict:
        letter_dict[word[i]].append(i)
    else:
        letter_dict[word[i]] = [i]
print(letter_dict)


# check if Ned wins
win = True
for letter in letters:
    if letter in letter_dict and letter_dict[letter]:
        del letter_dict[letter]
        if not letter_dict or not any(letter_dict.values()):
            break
    else:
        win = False
        break

# print output
if win:
    print("WIN")
else:
    print("LOSE")
