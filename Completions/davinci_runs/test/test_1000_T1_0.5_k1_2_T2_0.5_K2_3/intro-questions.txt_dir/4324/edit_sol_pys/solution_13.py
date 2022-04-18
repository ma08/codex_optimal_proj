# ----- Solution -----

t = int(input())
for i in range(t):
    n, a, b = map(int, input().split())
    s = ''
    if n == a and b == 1:
        print('a'*n)
    elif n == a+1 and b == 1:
        print('a'*(n-1)+'b')
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
