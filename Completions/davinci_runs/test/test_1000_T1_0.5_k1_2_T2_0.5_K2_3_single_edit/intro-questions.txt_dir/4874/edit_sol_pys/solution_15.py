

n = int(input())
s = input()
m = int(input())

if m == 1:
    print('YES')
    exit()

if n == m:
    print('NO')
    exit()

if s[0] == s[-1]:
    print('YES')
else:
    print('NO')
