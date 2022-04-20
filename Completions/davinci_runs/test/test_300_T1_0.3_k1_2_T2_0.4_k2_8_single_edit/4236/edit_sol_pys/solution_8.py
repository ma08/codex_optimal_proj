n, m = map(int, input().split())
left = [0] * (m + 1)
right = [0] * (m + 1)
for i in range(n):
    l, r = map(int, input().split())
    left[l] += 1
    right[r] += 1
ans = []
for i in range(1, m + 1):
    left[i] += left[i - 1]
    right[i] += right[i - 1]
for i in range(1, m + 1):
    if left[i] == right[i]:
        ans.append(i)
print(len(ans))
print(*ans)


n, m = map(int, input().split())

left = [0] * (m + 1)
right = [0] * (m + 1)

for i in range(n):
    l, r = map(int, input().split())
    left[l] += 1
    right[r] += 1

ans = []

for i in range(1, m + 1):
    left[i] += left[i - 1]
    right[i] += right[i - 1]

for i in range(1, m + 1):
    if left[i] == right[i]:
        ans.append(i)

print(len(ans))
print(*ans)
