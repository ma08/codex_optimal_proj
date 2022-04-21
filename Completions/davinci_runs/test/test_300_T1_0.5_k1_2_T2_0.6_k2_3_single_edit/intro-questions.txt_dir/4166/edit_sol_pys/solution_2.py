N, K = map(int, input().split())
S = input()


if K == 1:
    print(S)
    exit()

ans = S[0]

for i in range(1, N):
    if S[i] != ans[-1]:
        ans += S[i]

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
