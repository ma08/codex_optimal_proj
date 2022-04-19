
n, k = map(int, input().split())
a = list(map(int, input().split()))

def count_divisible(x):
    count = 0
    for i in range(n):
        if (x * 10**len(str(a[i])) + a[i]) % k == 0:
            count += 1
    return count

total = 0
for i in range(n):
    total += count_divisible(a[i])

print(total)
