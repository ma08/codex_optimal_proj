

N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

count = 0

for i in range(1, M + 1):
    for j in range(N):
        if i not in A[j][1:]:
            break
    else:
        count += 1

print(count)
