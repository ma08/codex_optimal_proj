

# ---- Input ---- 
# A B C
# 5 7 5

# ---- Output ----
# 7
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
