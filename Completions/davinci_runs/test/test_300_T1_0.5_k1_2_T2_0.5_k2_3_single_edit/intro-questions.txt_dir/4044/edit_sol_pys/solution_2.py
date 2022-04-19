

a, b, x = map(int, input().split())

s = "0"*a + "1"*b

for i in range(a):
    for j in range(b):
        if i + j == x:
            print(s)
            exit()

print("-1")
        s = s[1:] + s[0]
