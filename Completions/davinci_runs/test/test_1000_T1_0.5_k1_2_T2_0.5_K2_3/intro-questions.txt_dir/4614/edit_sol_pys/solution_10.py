
# ---- Input ----
# A B C
# 5 7 5

# ---- Output ----
# 7

# ---- Answer ----

# get input
a, b, c = map(int, input().split())

# if a == b
if a == b:
    print(c)

# if a == c
elif a == c:
    print(b)

# if b == c
elif b == c:
    print(a)
