

# Solution

n, k = map(int, input().split())
a = list(map(int, input().split()))

mod_counts = [0] * k
for x in a:
    mod_counts[x % k] += 1

count = 0
if mod_counts[0] > 1:
    count += mod_counts[0] * (mod_counts[0] - 1) // 2
for i in range(1, k // 2 + 1):
    if i == k - i:
        count += mod_counts[i] * (mod_counts[i] - 1) // 2
    else:
        count += mod_counts[i] * mod_counts[k - i]

print(count)