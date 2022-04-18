
y, p = input().split()

if p[-1] == 'x':
    print(p + y)
elif p[-1] == 'e':
    print(p + 'x' + y)
elif p[-1] in 'aiou':
    print(p[:-1] + 'ex' + y)
elif p[-2:] == 'ex':
    print(p + y)
