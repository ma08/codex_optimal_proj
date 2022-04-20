

a, b, x = map(int, input().split())
s = '1'*b + '0'*a

for i in range(a):
    for j in range(b):
        if i + j == x:
            print(s)
            exit()
        s = s[1:] + s[0]
