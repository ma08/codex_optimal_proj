

y, p = input().split()

if y[-1] == 'e':
    print(y + 'x' + p)
elif y[-1] in 'aiou':
    print(y[:-1] + 'ex' + p)
    print(y + p)
elif y[-2:] == 'ex':
else:
    print(y + 'ex' + p)
