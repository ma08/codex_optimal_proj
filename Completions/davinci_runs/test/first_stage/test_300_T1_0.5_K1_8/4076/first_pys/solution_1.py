

import math

def analog_clock(A, B, H, M):
    hour_hand_angle = (H % 12) * 30 + M * 0.5
    minute_hand_angle = M * 6
    if hour_hand_angle == minute_hand_angle:
        return 0
    else:
        angle = abs(hour_hand_angle - minute_hand_angle)
        if angle > 180:
            angle = 360 - angle
        angle_radian = math.radians(angle)
        return math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(angle_radian))

if __name__ == '__main__':
    A, B, H, M = map(int, input().split())
    print(analog_clock(A, B, H, M))