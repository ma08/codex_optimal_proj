

# ==========
# Solution 1
# ==========
s, w = map(int, input().split())

if s <= w:
    print("unsafe")
else:
    print("safe")

# ==========
# Solution 2
# ==========
s, w = map(int, input().split())

print("unsafe" if s <= w else "safe")