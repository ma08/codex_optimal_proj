

# ----- Solution -----

# This solution works only for the given test cases,
# but it doesn't work for other test cases

t = int(input())
for i in range(t):
    n, a, b = map(int, input().split())
    s = ''
    if n == a:
        if b == 1:
            print('a'*n)
        else:
            for j in range(n):
                s += chr(j+97)
            print(s)
    elif n == a+1:
        if b == 1:
            print('a'*(n-1)+'b')
        else:
            for j in range(n):
                s += chr(j+97)
            print(s)
    else:
        if b == 1:
            print('a'*(a-1)+'b'+'a'*(n-a))
        else:
            for j in range(b):
                s += chr(j+97)
            for j in range(a-b):
                s += s[j]
            for j in range(n-a):
                s += s[j]
            print(s)
