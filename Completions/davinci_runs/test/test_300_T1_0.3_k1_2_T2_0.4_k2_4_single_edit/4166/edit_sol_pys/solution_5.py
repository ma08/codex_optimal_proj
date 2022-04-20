
N, M = map(int, input().split())

s = []
c = []
for _ in range(M):
    s_i, c_i = map(int, input().split())
    s.append(s_i)
    c.append(c_i)
ans = -1
for i in range(10**N):
    i_str = str(i)
    if len(i_str) != N:
        continue
    for j in range(M):
        if i_str[s[j]-1] != str(c[j]):
            break
    else:
        ans = i
        break

print(ans)
