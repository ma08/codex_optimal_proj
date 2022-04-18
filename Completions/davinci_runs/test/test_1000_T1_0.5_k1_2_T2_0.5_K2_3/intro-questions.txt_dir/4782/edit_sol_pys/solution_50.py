
 
n, m = [int(i) for i in input().split()]

if m == n - 1:
    print(m)
elif m <= n:
    print(m + 1)
else:
    print(n + (m - n) // 2)
