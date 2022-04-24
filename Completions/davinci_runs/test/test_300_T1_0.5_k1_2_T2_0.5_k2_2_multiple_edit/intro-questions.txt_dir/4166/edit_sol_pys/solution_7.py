
N, M = map(int, input().split())

S = []
C = []

for i in range(M):
    tmp = list(map(int, input().split()))
    S.append(tmp[0])
    C.append(tmp[1])

min_num = 0
max_num = 10 ** N

for i in range(min_num, max_num):
    num_str = str(i)
    if len(num_str) != N:
        continue
    is_match = True
    for j in range(M):
        if int(num_str[S[j]-1]) != C[j]:
            is_match = False
            break
    if is_match:
        print(i)
        exit()

print(-1)
