

y, p = input().split()

if y[-1] == 'e' or y[-1] in 'aeiou':
    if y[-1] == 'e':
        print(y + 'x' + p)
    else:
        print(y[:-1] + 'ex' + p)
else: print(y + p)
