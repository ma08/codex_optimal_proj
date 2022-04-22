

# a, b, k = map(int, input().split())
a, b, k = 2, 3, 3
# a, b, k = 1000000000000, 1000000000000, 1000000000000

if a >= k:
    b = b
else:
    k = k - a
    a = 0 
    b = b - k

print(a, b)
