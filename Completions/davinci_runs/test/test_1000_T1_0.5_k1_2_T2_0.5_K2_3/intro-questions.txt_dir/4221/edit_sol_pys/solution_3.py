s = input()
if s[-1] == 's' and s[-2] != 's':
    print(s + 'es')
else:
    print(s + 's')
