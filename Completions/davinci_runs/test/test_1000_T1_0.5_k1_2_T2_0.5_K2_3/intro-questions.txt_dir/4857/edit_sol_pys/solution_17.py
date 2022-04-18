from itertools import combinations

l, w = map(int, input().split())  # l is the number of letters, w is the word length

letters = 'abcdefghijklmnopqrstuvwxyz'  # all possible letters

for i in range(1, 26):  # number of letters to be used
    if i * l == w:  # if number of letters * letter length = word length, then it is possible to make a word
        print(letters[i - 1] * l)
        break
    elif i * l > w:  # if number of letters * letter length > word length, then it is possible to make a word
        poss = []  # list of possible words
        for j in range(i - 1, 0, -1):
            for com in combinations(letters[j - 1], l):  # generate all possible combinations of letters
                if sum(com) == w:
                    poss.append(com)  # if the sum of the word is equal to the word length, then add it to the list
        if len(poss) > 0:
            print(''.join(poss[0]))  # print the first possible word
            break
        else:
            print('impossible')  # if there are no possible words, then print impossible
            break
