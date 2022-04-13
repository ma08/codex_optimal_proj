

s = input()

if s[-1] == 'e':
    print(s + 'x' + 'ay', end=' ')
elif s[-1] in 'aiou':
    print(s[:-1] + 'ex' + 'ay', end=' ')
else:
    print(s + 'ay', end=' ')
