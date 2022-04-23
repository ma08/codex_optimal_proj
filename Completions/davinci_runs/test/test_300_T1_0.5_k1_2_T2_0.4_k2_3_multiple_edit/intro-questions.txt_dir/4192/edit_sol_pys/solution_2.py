
d, t, s = map(float, input().split())

if d / s <= t:  # 到達地点までの時間がちょうど時間内かどうかを判定
    print("Yes")
else:
    print("No")
