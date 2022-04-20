

# ==========
# Solution 1
# ==========

a, b = list(map(int, input().split()))

if a > b:
    a, b = b, a

print(a)
