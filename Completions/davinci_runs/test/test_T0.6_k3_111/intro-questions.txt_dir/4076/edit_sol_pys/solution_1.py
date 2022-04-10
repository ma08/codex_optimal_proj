
from math import pi, cos, sin

def get_answer(A, B, H, M):
    hour_angle = (H + M / 60) * (360 / 12) * (pi / 180)  # 時針の角度
    minute_angle = M * (360 / 60) * (pi / 180)  # 分針の角度

    x1 = A * cos(hour_angle)  # 時針のx座標
    y1 = A * sin(hour_angle)  # 時針のy座標
    x2 = B * cos(minute_angle)  # 分針のx座標
    y2 = B * sin(minute_angle)  # 分針のy座標
    return ((x2-x1)**2 + (y2-y1)**2)**0.5  # 時針と分針の距離

def main():
    A, B, H, M = map(int, input().split())
    print("{:.20f}".format(get_answer(A, B, H, M)))

if __name__ == '__main__':
    main()
