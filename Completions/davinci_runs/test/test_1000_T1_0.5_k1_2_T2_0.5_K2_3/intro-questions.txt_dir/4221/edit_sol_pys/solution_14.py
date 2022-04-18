

s = input()
    print(s[:-1] + 'es')
if s[-1] == 's':
elif s[-1] == 'y':
    print(s[:-1] + 'ies')
else:
    print(s + 's')
