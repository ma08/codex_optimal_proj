
n, k = map(int, input().split())
a = list(map(int, input().split()))

def concat(x, y): return (x * 10**len(str(y))) + y

def count_divisible(x): return sum(1 for i in range(n) if concat(x, a[i]) % k == 0)

total = 0
for i in range(n):
    total += count_divisible(a[i])

print(total)
