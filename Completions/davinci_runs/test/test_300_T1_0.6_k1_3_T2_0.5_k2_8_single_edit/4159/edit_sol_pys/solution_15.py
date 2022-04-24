

a, b, k = map(int, input().split()) # 標準入力から整数値を受け取る
a -= min(a, k) # a - min(a, k)
k -= min(a+b, k) # k - min(a+b, k)
b -= min(b, k) # b - min(b, k)
print(a, b) # a, bを出力
