# https://atcoder.jp/contests/abc086/tasks/abc086_b

a, b = map(int, input().split())

if int(str(a)+str(b))**(1/2) % 1 == 0:
    print("Yes")
else:
    print("No")
print(n//2 + cnt)
