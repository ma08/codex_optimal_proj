

# ---- Input ----
# A B C D
# 5 7 5 7

# ---- Output ----
# 5

# ---- Answer ----

# get input
a, b, c, d = map(int, input().split())

# check a == d
if a == d:
    print(b)

# check b == d
elif b == d:
    print(b)

# check c == d
elif c == d:
    print(a)
