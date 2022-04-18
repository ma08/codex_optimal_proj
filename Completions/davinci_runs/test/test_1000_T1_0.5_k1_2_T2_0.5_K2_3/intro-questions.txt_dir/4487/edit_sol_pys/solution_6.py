# https://codeforces.com/contest/1183/problem/A

# input
a, b, c = map(int, input().split())

# check
if a[-1] == b[0] and b[-1] == c[0] and a + b == c:
    print("YES")
else:
    print("NO")
