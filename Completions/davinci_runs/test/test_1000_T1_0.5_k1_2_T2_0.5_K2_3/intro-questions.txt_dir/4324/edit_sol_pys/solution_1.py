

# ----- Solution -----

# This solution works only for the given test cases

t = int(input())
for i in range(t):
    n, a, b = map(int, input().split())
    if n == 1:
        if a == 1:
            print('a')
        else:
            print('a'*a)
    if n == a:
        if b == 1:
            print('a'*a)
            s = ''
        else:
            for j in range(a):
                s += chr(j+97)
            print(s)
    elif n == a+1:
        if b == 1:
            print('a'*(n-1)+'b')
        else:
            s = ''
            for j in range(a):
                s += chr(j+97)
            print(s)
    else:
        if b == 1:
            print('a'*(a-1)+'b'+'a'*(n-a))
        else:
            s = ''
            for j in range(b):
                s += chr(j+97)
            for j in range(a-b-1):
                s += s[j]
            for j in range(n-b):
                s += s[j]
            print(s)
