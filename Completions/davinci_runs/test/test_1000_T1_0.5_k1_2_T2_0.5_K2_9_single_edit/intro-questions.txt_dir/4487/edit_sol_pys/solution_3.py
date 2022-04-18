

# input
a, b, c = input().split() # a, b, c = raw_input().split() for Python 2.7

# check
if a[-1] == b[0] and b[-1] == c[0]:
    print("YES")
else:
    print("NO")
