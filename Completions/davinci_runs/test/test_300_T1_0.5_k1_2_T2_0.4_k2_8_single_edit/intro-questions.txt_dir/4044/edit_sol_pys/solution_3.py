

a, b, x = map(int, input().split())

s = "0"*b + "1"*a

for i in range(a):
    for j in range(a):
        if i + j == x-1:
            print(s)
            exit()
        s = s[1:] + s[0]
