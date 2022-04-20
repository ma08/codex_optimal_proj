
n, k = map(int, input().split())  # map(関数, イテレータ)
s = input()  # 文字列

if k > n or k == 0:
    print(-1)
else:
    print(n - k)
