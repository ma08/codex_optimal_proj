

y, p = input().split() #input two strings

if y[-1] == 'e': #if the last letter of the first string is e, add x
    print(y + 'x' + p)
elif y[-1] in 'aiou':
    print(y[:-1] + 'ex' + p)
else:
    print(y + p)
