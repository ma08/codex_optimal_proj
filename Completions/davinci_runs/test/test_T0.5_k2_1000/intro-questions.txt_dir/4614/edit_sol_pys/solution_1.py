
# ---- Input ----
# A B C
# 5 7 5
# ---- Output ----
# 7
# ---- Answer ----
# get input
a, b, c = map(int, input().split())
# check a == b and print c
if a == b:
    print(c)
# check a == c and print b
elif a == c:
    print(b)
# check b == c and print a
elif b == c:
    print(a)
