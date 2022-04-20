

a, b, x = map(int, input().split())
s = "0"*a + "1"*b  # 全部0のときと全部1のときを考える

for i in range(a):
    for j in range(b):
        if i + j == x:
            print(s)
            exit()
        s = s[1:] + s[0]
