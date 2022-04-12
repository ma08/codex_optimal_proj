

y, p = input().split()  # y = word, p = prefix

if y[-1] == 'e':  # if the word ends with 'e'
    print(y + 'x' + p)
elif y[-1] in 'aiou':
    print(y[:-1] + 'ex' + p)
elif y[-2:] == 'ex':
    print(y + p)
