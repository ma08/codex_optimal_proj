N, M = map(int, input().split())
s, c = [], []
for i in range(M):
    s_i, c_i = map(int, input().split())
    s.append(s_i)
    c.append(c_i)
min_num = 0
max_num = 10**N
for i in range(min_num, max_num):
    is_match = True
    for j in range(M):
        if str(i)[s[j]-1] != str(c[j]):
            is_match = False
            break
    if is_match:
        print(i)
        exit()
print(-1)
