
n = int(input())
a = list(map(int, input().split()))

if a.count(a[0]) == n:
    print("YES")  # すべての要素が同じ場合はYES
    exit()  # 終了

a_sorted = sorted(a)

for i in range(n - 1):
    if a_sorted[i] + 1 != a_sorted[i + 1]:
        print("NO")  # 一つでも隣り合う要素が連続しない場合はNO
        exit()  # 終了

print("YES")  # ここまで来ていれば、隣り合う要素が全て連続しているのでYES
