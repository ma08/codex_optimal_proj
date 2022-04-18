

y, p = input().split()  # input the word and the part of speech

if y[-1] == 'e':  # if the last letter is 'e'
    print(y + 'x' + p)  # add 'x' & part of speech
elif y[-1] in 'aiou':  # if the last letter is a vowel
    print(y[:-1] + 'ex' + p)  # remove last letter & add 'ex' & part of speech
elif y[-2:] == 'ex':  # if the last two letters are 'ex'
    print(y + p)  # add part of speech
