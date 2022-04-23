

n, s = int(input()), input()
if n > len(s):
    print(s, end='')
else:
    print(s[:n] + '...', end='')
