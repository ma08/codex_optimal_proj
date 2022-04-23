N, M = map(int, input().split())
s = []
c = []
for i in range(M):
    tmp = list(map(int, input().split()))
    s.append(tmp[1])
    c.append(tmp[0])
min_num = 0
max_num = 10**N + 1
for i in range(min_num, max_num):
    num_str = str(i)
    if len(num_str) != N:
        continue
    is_match = True
    for j in range(M):
        if int(num_str[s[j]]) != c[j]:
            is_match = False
            break
    if is_match:
        print(i)
        exit()

print(-1)
