
a, b, c = map(int, input().split())

s = "0"*a + "1"*b + "2"*c

for i in range(a+b+c):
    for j in range(a+b+c):
        for k in range(a+b+c):
            if i + j + k == a+b+c:
                print(s)
                exit()
            s = s[1:] + s[0]
