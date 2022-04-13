

n, X = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
count = 0
for i in range(n):
    if prices[i] > X:
        count += 1

print(count)
