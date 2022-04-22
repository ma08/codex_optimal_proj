

# Solution

N, K = [int(x) for x in input().split()]
S = input()

left = 0
right = K
count = 0
for i in range(N):
    if S[i] == '1':
        continue
    count += 1
    if i < left:
        continue  # skip
    if left <= right:
        right = min(N - 1, right + K - 1)
    if right < i:
        left = min(left + K, N - 1)
        right = min(right + K, N - 1)
print(count)

print(cost)
