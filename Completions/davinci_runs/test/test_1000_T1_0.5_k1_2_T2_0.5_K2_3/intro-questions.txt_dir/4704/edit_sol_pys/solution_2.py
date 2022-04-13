N, K = map(int, input().split())  # N個のボールがあり、K個選ぶ
A = list(map(int, input().split()))  # 各ボールの重さ
A.sort()  # 重さの昇順に並べる
for i in range(N):  # ボールを順番に見ていく
    if K <= A[i]:  # Kがボールの重さより小さければ終わり
        print(i)  # i個目のボールが残りのKを超えたため、i個選ぶ
        exit()  # 終了
    else:  # Kがボールの重さより大きければ
        K -= A[i]  # Kからボールの重さを減らす
