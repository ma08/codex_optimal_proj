
a, b, x = map(int, input().split())

s = "0"*a + "1"*b 

for i in range(a+b):
    if s.count("0") == x:
        print(s)
        exit()
    s = s[1:] + s[0]
