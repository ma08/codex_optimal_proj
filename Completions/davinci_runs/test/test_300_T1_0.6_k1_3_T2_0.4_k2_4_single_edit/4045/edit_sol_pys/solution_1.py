

n = int(input())
s = input()
t = input()

if s[0] == t[0]:
    print('YES')
    print('a'*n + 'b'*n + 'c'*n, flush=True)
elif s[0] == t[1]:
    print('YES')
    print('a'*n + 'c'*n + 'b'*n, flush=True)
elif s[1] == t[0]:
    print('YES')
    print('c'*n + 'a'*n + 'b'*n, flush=True)
elif s[1] == t[1]:
    print('YES')
    print('c'*n + 'b'*n + 'a'*n, flush=True)
else:
    print('NO')
