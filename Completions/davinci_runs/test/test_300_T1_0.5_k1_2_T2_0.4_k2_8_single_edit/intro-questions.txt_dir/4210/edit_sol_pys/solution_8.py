
n, k = map(int, input().split())
a = list(map(int, input().split()))

def concat(x, y, k):
    return (x * 10**k) + y

def count_divisible(x, k):
    count = 0
    for i in range(n):
        if concat(x, a[i], k) % k == 0:
            count += 1
    return count

total = 0
for i in range(n):
    total += count_divisible(a[i])

print(total)
