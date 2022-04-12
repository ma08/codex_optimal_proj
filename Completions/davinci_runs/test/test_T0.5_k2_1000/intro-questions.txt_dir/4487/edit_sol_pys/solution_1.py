

# input
a, b, c = input().split()  # input a b c

# check
if a[-1] == b[0] and b[-1] == c[0]:
    print("YES")
else:
    print("NO")
