
y, p = input().split()
if y[-1] == 'e':
    print(y + 'x' + p) #x
elif y[-1] in 'aiou':
    print(y[:-1] + 'ex' + p)
else:
    print(y + p)
