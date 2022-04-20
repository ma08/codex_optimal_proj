

n = int(input())
a = list(map(int, input().split()))

# The number of elements in the longest increasing subarray
# ending at the current position
inc = [1] * n

# The number of elements in the longest decreasing subarray
# ending at the current position
dec = [1] * n

# The number of elements in the longest increasing subarray
# ending at the current position and including the current element
inc_cur = [1] * n

# The number of elements in the longest decreasing subarray
# ending at the current position and including the current element
dec_cur = [1] * n

for i in range(1, n):
    if a[i] > a[i - 1]:
        inc[i] = inc[i - 1] + 1
    if a[i] < a[i - 1]:
        dec[i] = dec[i - 1] + 1
    inc_cur[i] = inc[i]
    dec_cur[i] = dec[i]
    if a[i] > a[i - 1]:
        inc_cur[i] = max(inc_cur[i], dec_cur[i - 1] + 1)
    if a[i] < a[i - 1]:
        dec_cur[i] = max(dec_cur[i], inc_cur[i - 1] + 1)

print(max(inc_cur[-1], dec_cur[-1]))