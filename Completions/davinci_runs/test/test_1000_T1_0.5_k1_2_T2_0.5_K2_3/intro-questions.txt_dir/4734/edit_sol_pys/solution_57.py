

y,p = input().split() # taking input from the user

if y[-1]=='e': # checking if the last letter is 'e'
    print(y + 'x' + p)
elif y[-1] in ['a','i','o','u']:
    print(y[:-1] + 'ex' + p)
elif y[-2:] == 'ex':
    print(y + p)
