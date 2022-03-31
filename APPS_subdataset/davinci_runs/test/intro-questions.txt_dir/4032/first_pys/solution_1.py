

n, k = map(int, input().split())
a = map(int, input().split())

left = 0
right = n - 1
score = 0

while left <= right:
    if a[left] <= k:
        score += 1
        left += 1
    elif a[right] <= k:
        score += 1
        right -= 1
    else:
        break

print(score)