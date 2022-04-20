

# SOLUTION

n = int(input())
arr = list(map(int, input().split()))

d = {}
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

count = 1
for i in d:
    count *= (d[i]+1)
    count %= 998244353

print(count)