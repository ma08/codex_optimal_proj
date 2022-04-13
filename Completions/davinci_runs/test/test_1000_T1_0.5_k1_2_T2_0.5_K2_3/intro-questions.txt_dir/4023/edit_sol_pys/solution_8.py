
n = int(input())
a = list(map(int, input().split()))

if a.count(a[0]) == n:  # a[0]が全ての要素と一致するか
    print("YES")
    exit()  # 一致するならYESを出力して終了

a_sorted = sorted(a)  # aを昇順にソートしてa_sortedに代入

for i in range(n - 1):
    if a_sorted[i] + 1 != a_sorted[i + 1]:  # i番目とi+1番目の差が1以外の時
        print("NO")
        exit()  # NOを出力して終了

print("YES")  # 上記の条件に当てはまらないならYESを出力
