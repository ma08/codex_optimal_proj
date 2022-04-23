# https://codeforces.com/contest/1230/problem/B

a, b, c = map(int, input().split())
if a + b == c or a + c == b or b + c == a:
    print("YES")
    print(1)
else:
    b = [0]*n
    for i in range(n):
        if a[i] == a[0]:
            b[i] = 1
        else:
            b[i] = 2
    if a[0] in a[1:]:
        print("NO")
    else:
        print("YES")
        print(*b)
