

s = input()
if s[-1] == 'y' and s[-2] not in 'aeiou':
    print(s[:-1] + 'ies')
else:
    print(s + 's')
