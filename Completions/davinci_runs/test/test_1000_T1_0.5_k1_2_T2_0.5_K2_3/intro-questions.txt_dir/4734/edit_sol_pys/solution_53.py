

y, p = raw_input().split()

if p[-1] == 'e':
    print(p + 'x' + y)
elif p[-1] in 'aeiou':
    print(p[:-1] + 'ex' + y)
elif p[-2:] == 'ex':
    print(p + y)
