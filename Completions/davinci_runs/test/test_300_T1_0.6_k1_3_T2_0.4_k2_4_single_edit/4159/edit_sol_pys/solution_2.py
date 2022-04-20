

a, b, k = map(int, input().split())  #a,b,kを受け取る

for i in range(k):  #k回ループ
    if a > 0:
        a -= 1
    elif b > 0:
        b -= 1

print(a, b)  #出力
