

n = int(input())
a = list(map(int, input().split()))

# sum of the powers of 2 from 0 to 30
pow_sum = [0]
for i in range(1, 31):
    pow_sum.append(2**i + pow_sum[i-1])

# iterate over all possible subsets of the array
# and check whether the sum of the elements of the subset
# is a power of 2, i.e. is in the array pow_sum
# if so, then the current subset is good
# and we can delete the remaining elements
ans = n
for i in range(1, 2**n):
    s = 0
    for j in range(n):
        if (i >> j) & 1:
            s += a[j]
    if s in pow_sum:
        ans = min(ans, n-bin(i).count('1'))

print(ans)