

N = int(input())  # 入力
L = list(map(int, input().split()))  # 入力

L.sort()  # 昇順に並び替え

if L[0] + L[1] > L[-1]:  # 最大値より小さい値の和が最大値より大きい場合
    print("Yes")  # 三角形が作れる
else:
    print("No")
