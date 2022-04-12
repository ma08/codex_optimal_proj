

y, p = input().split() # y = word, p = punctuation

if y[-1] == 'e':
    print(y + 'x' + p)
elif y[-1] in 'aeiou':
    print(y[:-1] + 'ex' + p)
else:
    print(y + p)
