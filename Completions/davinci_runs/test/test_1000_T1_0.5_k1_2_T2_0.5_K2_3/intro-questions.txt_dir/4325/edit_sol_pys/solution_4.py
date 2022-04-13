
n, x, t = map(int, input().split())  # 入力を分割して取得

if n % x == 0:  # おつりが出ない場合
    print(t * (n // x))
else:  # おつりが出る場合
    print(t * (n // x + 1))
