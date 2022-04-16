

a, b, x = map(int, input().split()) # a=0, b=1, x=1

s = "0"*a + "1"*b # s = "01"

for i in range(a):
    for j in range(b):
        if i + j == x:
            print(s)
            exit()
        s = s[1:] + s[0] # s = "10"
