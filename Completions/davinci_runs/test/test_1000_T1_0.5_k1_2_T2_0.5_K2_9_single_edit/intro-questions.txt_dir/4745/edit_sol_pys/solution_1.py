
n, x = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()

left = 0
right = n - 1

result = 0
while left < right:
    right -= 1

while left < right:
    right -= 1
    if prices[left] + prices[right] > x:
        result += 1
    left += 1

if left == right:
    if prices[left] > x:
        result += 1

print(result)
