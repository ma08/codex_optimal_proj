
# 入力
N = int(input())
c = []
s = []
f = []
for i in range(N-1):
    c, s, f = map(int, input().split())
    c.append(c)
    s.append(s)
    f.append(f)

# 出力
for i in range(N):
    t = 0
    for j in range(i, N-1):
        if t < s[j]:
            t = s[j]
        else:
            t = t + f[j] - t % f[j]
        t += c[j]
    print(t)
