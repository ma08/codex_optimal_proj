
a = input()
if sum(list(map(int, a.split()))) >= 22:
    print('bust')
else:
    print('win')
