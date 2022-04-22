

s = input()
if s[-1] == 's' or s[-1] == 'o' or s[-1] == 'x' or (s[-2] == 'c' and s[-1] == 'h') or (s[-2] == 's' and s[-1] == 'h'):
    print(s + 'es')
else:

    print(s + 's')
