

# initial input
a, b, c = map(int, input().split())  # a: 初期値, b: 最大値, c: 加算回数

# count up
count = 0
while b >= a and count < c:  # 条件を満たす間は加算を繰り返す
    b -= a
    count += 1

# output
print(count)  # 加算回数を出力する
