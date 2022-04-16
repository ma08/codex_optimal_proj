
y,p = input().split() #input the string

if y[-1]=='e':
    print(y+'x'+p)
elif y[-1] in ['a','i','o','u']:
    print(y[:-1]+'ex'+p)
elif y[-2:]=='ex':
    print(y+p)
