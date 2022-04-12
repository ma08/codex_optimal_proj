

y,p = input().split() # y is the word, p is the phrase,

if y[-1]=='e': # if the word ends in e
    print(y+'x'+p)
elif y[-1] in ['a','i','o','u']:
    print(y[:-1]+'ex'+p)
elif y[-2:]=='ex':
    print(y+p)
