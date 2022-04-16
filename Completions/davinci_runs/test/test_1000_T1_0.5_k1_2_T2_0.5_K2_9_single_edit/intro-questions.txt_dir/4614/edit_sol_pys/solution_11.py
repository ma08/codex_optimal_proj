

# ---- Input ----
# 5 5 7

# ---- Output ----
# 5

# ---- Answer ----

# get input
a, b, c = map(int, input().split())

# check a == b
if a == b:
    print(c)

# check a == c
elif a == c:
    print(b)

# check b == c
elif b == c:
    print(a)
