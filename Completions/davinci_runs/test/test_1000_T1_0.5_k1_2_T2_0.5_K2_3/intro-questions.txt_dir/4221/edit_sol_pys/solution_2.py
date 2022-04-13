

s = input()
if s[-1] == 's':
    print(s + 'es')
elif s[-1] == 'y' and s[-2] not in 'aeiou':
    print(s[:-1] + 'ies')
    print(s + 'es')
else:
    print(s + 's')
