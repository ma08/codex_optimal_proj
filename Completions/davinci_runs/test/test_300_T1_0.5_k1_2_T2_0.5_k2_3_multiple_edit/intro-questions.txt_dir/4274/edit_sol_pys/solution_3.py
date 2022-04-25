
# yes or no
N, M = map(int, input().split())

if N == M:
    print("Yes")
else:
    print("No")

# sum
N = int(input())
A = list(map(int, input().split()))

sum = 0
for i in range(N):
    sum += A[i]
print(sum)
