

# -----Answer-----

k = int(input())
s = str(input())

# -----Answer-----
print(s[:k] + '...' if len(s) > k else s)
