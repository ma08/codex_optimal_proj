

a, b, x = map(int, input().split()) # 横に並べる白いボールの数、横に並べる黒いボールの数、横に並べるボールの数
ans = []
s = "0"*a + "1"*b # 白いボールは0、黒いボールは1とする

for i in range(a):
    for j in range(b):
        if i + j == x:
            ans.append(s)

print(sorted(ans)[0])
        s = s[1:] + s[0]
