

s = input()
if s[-1] == 's' or s[-1] == 'S':
    print(s + 'es' if s.islower() else s + 'ES')
else:
    print(s + 's' if s.islower() else s + 'S')
