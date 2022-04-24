

N, M = map(int, input().split())
prefecture = [[] for _ in range(N+1)]

for i in range(M):
    P, Y = map(int, input().split())
    prefecture[P].append(Y)

    prefecture[i].sort()
for i in range(1, N+1):
    for j in range(len(prefecture[i])):
        print(str(i).zfill(6) + str(j+1).zfill(6))
