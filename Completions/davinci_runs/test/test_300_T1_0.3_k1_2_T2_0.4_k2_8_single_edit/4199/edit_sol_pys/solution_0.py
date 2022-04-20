

N, M, X = map(int, input().split())
A = list(map(int, input().split()))

count1 = 0
count2 = 0
for i in range(N):
    if A[i] < X:
        count1 += 1
    else:
        count2 += 1

print(min(count1, count2))
