

import math

# Set up
A, B, H, M = map(int, input().split())  # A, B: 直角の辺, H, M: 時間

# Solve
theta_h = H * 360 / 12  # 時針の角度
theta_m = M * 360 / 60  # 分針の角度
theta_hm = theta_h - theta_m

if theta_hm < 0:
    theta_hm = 360 + theta_hm  # 時針の角度が小さいとき

theta_hm = theta_hm * math.pi / 180

c = A * A + B * B - 2 * A * B * math.cos(theta_hm)  # 余弦定理
c = math.sqrt(c)

# Output
print(c)  # 出力
