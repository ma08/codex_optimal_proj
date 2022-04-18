
y,p = input().split()

if y[-1] == 'e':
    print(y + 'ex' + p)
elif y[-1] in ['a', 'i', 'o', 'u']:
    print(y[:-1] + 'ex' + p)
elif y[-2:] == 'ex':
    print(y + p)
