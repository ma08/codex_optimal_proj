N, M = map(int, input().split())
A = [0] * N
for _ in range(M):
    s, c = map(int, input().split())
    A[s-1] = c


N, M = map(int, input().split())

s = []
c = []

for i in range(M):
    tmp = list(map(int, input().split()))
    s.append(tmp[0])
    c.append(tmp[1])

min_num = 0
max_num = 10**N

for i in range(min_num, max_num):
    num_str = str(i)
    if len(num_str) != N:
        continue
    is_match = True
    for j in range(M):
        if int(num_str[s[j]-1]) != c[j]:
            is_match = False
            break
    if is_match:
        print(i)
        exit()

print(-1)
