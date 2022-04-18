n, x, t = map(int, input().split())  # 分割数と個数と時間

if n % x == 0:  # 分割数が個数で割り切れる時
    print(t * (n // x))  # 時間×分割数÷個数
else:
    print(t * (n // x + 1))  # 時間×分割数÷個数+1
