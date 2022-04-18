

y,p = input().split()

if y[-1] == 'e' and y[-2:] != 'ex':
    print(y + 'x' + p)
elif y[-1] in ['a', 'i', 'o', 'u'] and y[-2:] != 'ex':
    print(y[:-1] + 'ex' + p)
elif y[-2:] == 'ex':
    print(y + p)
