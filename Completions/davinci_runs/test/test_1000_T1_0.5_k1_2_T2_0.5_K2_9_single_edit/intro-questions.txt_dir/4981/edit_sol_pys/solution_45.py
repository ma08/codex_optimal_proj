
N = int(input())
A = list(map(int, input().split()))
answer = 0
for i in range(N):
    answer += A[i] - 1
print(answer)
