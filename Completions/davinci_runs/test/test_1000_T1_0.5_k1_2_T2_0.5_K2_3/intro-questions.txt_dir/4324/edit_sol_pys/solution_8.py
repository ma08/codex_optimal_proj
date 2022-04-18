

# ----- Solution -----
s = ''
# This solution works only for the given test cases

t = int(input())
for i in range(t):
    n, a, b = map(int, input().split())
    if n == 1:
        if a == 1:
            print('a')
        else:
            print('a'*a)
    elif n == a:
        if b == 1:
            print('a'*a)
        else:
            for j in range(a):
                s += chr(j+97)
            print(s)
    elif n == a+1:
        if b == 1:
            print('a'*(n-1)+'b')
        else:
            for j in range(a):
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
            for j in range(n-b):
                s += s[j]
            print(s)
