

H, N = map(int, input().split())  # 入力を受け取る
A = list(map(int, input().split()))  # 入力を受け取る

if sum(A) >= H:  # 条件に合っているか
    print('Yes')
else:
    print('No')
