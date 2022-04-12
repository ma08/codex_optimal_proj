
a, b, c = map(int, input().split())
k = int(input()) # 操作回数
if k % 2 == 1:
    print(a * 2 ** k + b + c)
else: # k % 2 == 0
    print(a + b + c)
