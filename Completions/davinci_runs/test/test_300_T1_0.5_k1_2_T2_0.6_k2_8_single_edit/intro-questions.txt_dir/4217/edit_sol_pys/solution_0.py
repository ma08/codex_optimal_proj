

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

# print(A)

# for i in range(N):
#     for j in range(A[i][0]):
#         print(A[i][j + 1], end=' ')
#     print()

count = 0

for i in range(1, M + 1):
    for j in range(N):
        if i not in A[j][1:]:
            break
    else:
        count += 1

print(count)
