

y, p = input().split()

if y[-1] == 'e':
    print(y+'x'+p, end=' ')
elif y[-1] in ['a', 'i', 'o', 'u']:
    print(y[:-1]+'ex'+p, end=' ')
elif y[-2:] == 'ex':
    print(y+p, end=' ')
else:
    print(y[:-1]+'ex'+p, end=' ')
