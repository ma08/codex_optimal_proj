from sys import stdin

n = int(stdin.readline().strip())
if n % 2 == 1:
    print('Alice')
else:
    print('Bob')
