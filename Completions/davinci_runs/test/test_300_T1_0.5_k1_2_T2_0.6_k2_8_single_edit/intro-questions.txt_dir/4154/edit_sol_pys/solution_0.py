
# My solution

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
