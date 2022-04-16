
y, p = input().split()  # input string

if y[-1] == 'e':
    print(y + 'x' + p)  # if the last letter of the word is 'e'
elif y[-1] in 'aiou':
    print(y[:-1] + 'ex' + p)
else:
    print(y + p)
