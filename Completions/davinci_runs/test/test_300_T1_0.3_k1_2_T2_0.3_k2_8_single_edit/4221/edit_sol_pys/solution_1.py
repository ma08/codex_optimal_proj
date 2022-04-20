
s = input()
if s[-1] == 's' or s[-1] == 'x':
    print(s + 'es', end='')
elif s[-1] == 'h' and s[-2] == 'c':
    print(s + 'es', end='')
elif s[-1] == 'h' and s[-2] == 's':
    print(s + 'es', end='')
elif s[-1] == 'y' and s[-2] != 'a' and s[-2] != 'i' and s[-2] != 'u' and s[-2] != 'e' and s[-2] != 'o':
    print(s[:-1] + 'ies', end='')
else:
    print(s + 's', end='')
