from itertools import combinations_with_replacement

l, w = map(int, input().split())  # length, weight

letters = 'abcdefghijklmnopqrstuvwxyz'  # letters

# check if there is a letter with the weight of the word
for i in range(1, 26):
    if i * l == w:
        print(letters[i - 1] * l)  # print the letter l times
        break
    elif i * l > w:  # if there is no letter with the weight of the word
        # check if there is a combination of letters that have the weight of the word
        poss = []
        for j in range(i - 1, 0, -1):  # check from the heaviest letter to the lightest
            for com in combinations_with_replacement(letters[j - 1], l):
                if sum(com) == w:  # add the combinations that have the weight of the word
                    poss.append(com)
        if len(poss) > 0:  # if there is a combination with the weight of the word
            print(''.join(poss[0]))  # print the first combination
            break
        else:  # if there is no combination with the weight of the word
            print('impossible')
            break  # stop the loop
