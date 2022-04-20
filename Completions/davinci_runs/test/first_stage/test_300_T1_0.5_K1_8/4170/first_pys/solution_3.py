

n = int(input())
arr = list(map(int, input().split()))

memo = [0] * n
memo[0] = 1

for i in range(1, n):
    if arr[i] > arr[i-1]:
        memo[i] = memo[i-1] + 1
    else:
        memo[i] = 1

print(max(memo))