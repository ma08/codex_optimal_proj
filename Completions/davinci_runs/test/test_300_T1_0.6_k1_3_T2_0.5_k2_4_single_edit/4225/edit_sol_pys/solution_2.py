# https://atcoder.jp/contests/abc087/tasks/abc087_b

a,b,c,k = map(int,input().split())

if k <= a:
    print(k)
elif k <= a+b:
    print(a)
else:
    print(a-(k-a-b))
