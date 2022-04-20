

N = int(input())
A = list(map(int, input().split()))

# max_diff = 0
# for i in range(N):
#     for j in range(i+1, N):
#         max_diff = max(max_diff, abs(A[i]-A[j]))
# print(max_diff)

max_diff = 0
min_a = A[0]
for i in range(1, N):
    max_diff = max(max_diff, A[i]-min_a)
    min_a = min(min_a, A[i])
print(max_diff)