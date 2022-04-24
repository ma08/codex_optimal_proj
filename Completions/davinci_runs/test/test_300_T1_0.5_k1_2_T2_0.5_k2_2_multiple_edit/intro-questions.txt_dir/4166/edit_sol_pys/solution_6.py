N, M = map(int, input().split())
if N == 1 and M == 0:
    print(0)
    exit()
s = []
c = []
for i in range(M):
    tmp = list(map(int, input().split()))
    s.append(tmp[0])
    c.append(tmp[1])
for i in range(10**(N-1), 10**N):
    num_str = str(i)
    is_match = True
    for j in range(M):
        if int(num_str[s[j]-1]) != c[j]:
            is_match = False
            break
    if is_match:
        print(i)
        exit()

print(-1)
