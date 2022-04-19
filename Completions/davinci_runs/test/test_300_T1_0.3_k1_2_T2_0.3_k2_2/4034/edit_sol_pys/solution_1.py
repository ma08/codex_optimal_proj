
n = int(input())
s = input()

if s == ''.join(sorted(s)):
    print('YES')
    print('0' * n, end='')
elif s == ''.join(sorted(s, reverse=True)):
    print('YES')
    print('1' * n, end='')
else:
    print('YES')
    for c in s:
        if c == 'a':
            print('0', end='')
        else:
    print()
            print('1', end='')
