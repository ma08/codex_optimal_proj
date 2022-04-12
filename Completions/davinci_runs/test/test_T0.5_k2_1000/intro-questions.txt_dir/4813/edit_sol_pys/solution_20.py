

word = input().upper()  # input word
permutation = input().upper()  # input permutation

word_dict = {}  # dictionary of letters in word
for letter in word:
    if letter not in word_dict:
        word_dict[letter] = 1
    else:
        word_dict[letter] += 1

guesses_left = 8  # number of guesses left
for letter in permutation:
    if letter in word_dict:  # if letter is in word
        word_dict[letter] -= 1
        if word_dict[letter] == 0:  # if letter is not in word
            word_dict.pop(letter)
            if len(word_dict) == 0:  # if word is guessed
                print('WIN')
                break
    else:  # if letter is not in word
        guesses_left -= 1
        if guesses_left == 0:  # if no guesses left
            print('LOSE')
            break
