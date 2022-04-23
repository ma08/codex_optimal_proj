import sys

N, M = map(int, input().split())

s = [0 for _ in range(M)]
c = [0 for _ in range(M)]

for i in range(M):
    tmp = list(map(int, input().split()))
    s[i] = tmp[0]
    c[i] = tmp[1]

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
        sys.exit()

print(-1)
