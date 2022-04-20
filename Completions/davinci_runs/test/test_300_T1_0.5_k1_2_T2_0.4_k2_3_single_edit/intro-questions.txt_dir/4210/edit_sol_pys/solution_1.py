
n, k = map(int, input().split())
a = list(map(int, input().split()))

def concat(x, y, z):
    return (x * 10**len(str(y))) + y + z

def count_divisible(x):
    count = 0
    for j in range(n):
        for i in range(n):
            if concat(x, a[i], a[j]) % k == 0:
                count += 1
    return count

total = 0
for i in range(n):
    total += count_divisible(a[i])

print(total)
