

word = input("Enter a word: ")
permutation = input("Enter a permutation: ")

word_dict = {}
for letter in word:
    if letter not in word_dict:
        word_dict[letter] = 1
    else:
        word_dict[letter] += 1

guesses_left = 10
for letter in permutation:
    if letter in word_dict:
        word_dict[letter] -= 1
        if word_dict[letter] == 0:
            word_dict.pop(letter)
            if len(word_dict) == 0:
                print("You win!")
                break
    else:
        guesses_left -= 1
        if guesses_left == 0:
            print("You lose!")
            break
