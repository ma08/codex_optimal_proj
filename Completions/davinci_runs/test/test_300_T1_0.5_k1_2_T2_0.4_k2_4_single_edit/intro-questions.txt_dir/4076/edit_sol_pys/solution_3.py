

# Set up input
A, B, H, M = map(int, input().split()) # A, B: 半径, H, M: 時刻

# Solve
theta_h = H * 360 / 12 # 時針の角度
theta_m = M * 360 / 60 # 分針の角度
theta_hm = theta_h - theta_m # 時針と分針の角度の差

if theta_hm < 0:
    theta_hm = 360 + theta_hm

theta_hm = theta_hm * math.pi / 180 # ラジアンに変換

c = A * A + B * B - 2 * A * B * math.cos(theta_hm)
c = math.sqrt(c)

# Output
print(c)
