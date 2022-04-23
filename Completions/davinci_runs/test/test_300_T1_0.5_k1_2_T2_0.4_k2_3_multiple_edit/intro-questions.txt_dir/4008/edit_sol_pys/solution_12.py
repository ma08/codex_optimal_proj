# https://codeforces.com/contest/1230/problem/B

a, b, c = map(int, input().split())
if a+b == c or a+c == b or b+c == a:
    print("Yes")
elif a == b == c:
    print("Yes")
else: print("No")
