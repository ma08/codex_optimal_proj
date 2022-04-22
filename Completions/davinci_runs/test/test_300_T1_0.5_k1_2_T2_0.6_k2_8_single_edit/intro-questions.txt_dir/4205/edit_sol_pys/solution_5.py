

n = int(input())
p = list(map(int, input().split()))

# まず、入力をソートする
p.sort()
# 次に、ソートした配列の中で、入力配列と異なる位置を記憶する
# その際、交換回数が2以下ならYES、そうでなければNOを出力する
count = 0
for i in range(n - 1):
    if p[i] != p[i + 1]:
        count += 1
if count <= 2:
    print("YES")
else
    print("NO")
