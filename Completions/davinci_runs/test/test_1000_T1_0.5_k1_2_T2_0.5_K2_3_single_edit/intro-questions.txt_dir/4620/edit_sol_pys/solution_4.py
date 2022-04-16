
n = int(input())
c = []
s = []
f = []
for i in range(n - 1):
    c_tmp, s_tmp, f_tmp = map(int, input().split())
    c.append(c_tmp)
    s.append(s_tmp)
    f.append(f_tmp)

for i in range(n):
    if i == n - 1:
        print(0)
        continue
    elif i == 0:
        t = s[0]
        for j in range(n - 1):
            if t % f[j] == 0:
                t += c[j]
            else:
                t += f[j] - t % f[j] + c[j]
        print(t)
    else:
        t = s[i]
        for j in range(i, n - 1):
            if t % f[j] == 0:
                t += c[j]
            else:
                t += f[j] - t % f[j] + c[j]
        print(t)
