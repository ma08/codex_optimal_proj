# https://codeforces.com/contest/1183/problem/A

# input
a, b, c = input().split()

# check
if a[-1] == b[0] and b[-1] == c[0] and int(a) + int(b) == int(c):
    print("YES")
else:
    print("NO")
