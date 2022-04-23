
# My solution 1

N, M = map(int, input().split())
Gates = []
for i in range(M):
    Gates.append(list(map(int, input().split())))

# print(Gates)

count = 0
for i in range(N):
    count1 = 0
    for j in range(M):
        if i + 1 >= Gates[j][0] and i + 1 <= Gates[j][1]:
            count1 += 1
    if count1 == M:
        count += 1

print(count)

# Other solution 1

N, M = map(int, input().split())
L = [0] * N
R = [0] * N

for i in range(M):
    l, r = map(int, input().split())
    L[l-1] += 1
    R[r-1] += 1

ans = 0
tmp = 0
for i in range(N):
    tmp += L[i]
    if tmp == M:
        ans += 1
    tmp -= R[i]

print(ans)
