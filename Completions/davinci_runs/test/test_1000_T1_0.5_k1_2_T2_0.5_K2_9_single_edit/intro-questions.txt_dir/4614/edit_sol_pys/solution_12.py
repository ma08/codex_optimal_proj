

# ---- Input ----
# A B C D
# 5 7 5 7

# ---- Output ----
# 7

# get input
a, b, c, d = map(int, input().split())

# check a == b
if a == b and a != c:
    print(c)

# check a == c
elif a == c and a != b:
    print(b)

# check b == c
elif b == c and b != a:
    print(a)

# check a == d
elif a == d and a != b and a != c:
    print(b)

# check b == d
elif b == d and b != a and b != c:
    print(a)

# check c == d
elif c == d and c != a and c != b:
    print(a)
