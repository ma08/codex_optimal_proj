

y,p = input().split()

if y[-1]=='e':
    print(y+'x'+p)
elif y[-1] in ['a','i','o','u']:
    print(y[:-1]+'ex'+p)
elif y[-2:]=='ex':
else:
    print(y+'ex'+p)
    print(y+p)
