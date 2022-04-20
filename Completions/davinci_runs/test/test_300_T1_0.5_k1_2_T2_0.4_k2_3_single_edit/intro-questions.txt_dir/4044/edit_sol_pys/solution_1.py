

a, b, x = map(int, input().split())  # a, b, x = (int(i) for i in input().split())

s = "0"*a + "1"*b  # s = "0"*a + "1"*b

for i in range(a):  # for i in range(a):
    for j in range(b):
        if i + j == x:  # if i + j == x:
            print(s)  # print(s)
            exit()  # exit()
        s = s[1:] + s[0]  # s = s[1:] + s[0]
