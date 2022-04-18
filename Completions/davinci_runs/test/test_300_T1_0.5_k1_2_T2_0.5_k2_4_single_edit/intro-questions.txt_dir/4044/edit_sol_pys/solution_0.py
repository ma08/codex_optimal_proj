

a, b, x = map(int, input().split())

s = "1"*a + "0"*b

if x > a+b or x < a:
    print(-1)
    exit()

for i in range(a+b):
    if i == x:
        print(s)
        exit()
    s = s[1:] + s[0]
