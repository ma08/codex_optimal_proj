

# ---- Input ----
# A B C D
# 5 7 5

# ---- Output ----
# D

# ---- Answer ----

# get input
a, b, c, d = map(int, input().split())

# check a == b
if a == b:
    print(d)

# check a == c
elif a == c:
    print(d)

# check b == c
elif b == c:
    print(d)

# check d == a
elif d == a:
    print(c)

# check d == b
elif d == b:
    print(c)

# check d == c
elif d == c:
    print(b)
