

s = input().split()

for i in s:
    if i[-1] == 'e':
        print(i + 'x' + 'ay', end=' '),
    elif i[-1] in 'aiou':
        print(i[:-1] + 'ex' + 'ay', end=' '),
    else:
        print(i + 'ay', end=' ')
