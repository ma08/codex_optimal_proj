
# ---- Input ----
# A B C
# 5 7 5

# ---- Output ----
# 7

# ---- Answer ----

# get input
a, b, c = map(int, input().split())

# check a and b
if a == b:
    print(c)

# check a and c
elif a == c:
    print(b)

# check b and c
elif b == c:
    print(a)
