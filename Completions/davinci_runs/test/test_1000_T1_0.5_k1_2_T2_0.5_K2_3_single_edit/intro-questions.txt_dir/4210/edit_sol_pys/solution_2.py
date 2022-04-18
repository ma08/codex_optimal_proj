
n, k = map(int, input().split())
a = list(map(int, input().split()))

def count_divisible(x, y):
    if (x * 10**len(str(y))) + y % k == 0:
        return 1
    return 0

def count_divisible(x):
    count = 0
    for i in range(n):
        if concat(x, a[i]) % k == 0:
            count += 1
    return count

total = 0
for i in range(n):
    total += count_divisible(a[i])

print(total)
