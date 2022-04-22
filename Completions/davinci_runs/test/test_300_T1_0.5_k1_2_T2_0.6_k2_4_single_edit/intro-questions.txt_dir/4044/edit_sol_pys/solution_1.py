

a, b, x = map(int, input().split())

s = "0"*b + "1"*a

for i in range(a + b):
    if i + b == x:
        print(s)
        exit()
    s = s[1:] + s[0]
