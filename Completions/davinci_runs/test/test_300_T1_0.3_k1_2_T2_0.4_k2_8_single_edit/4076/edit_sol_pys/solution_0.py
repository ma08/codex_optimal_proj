


import math

def main():
    A, B, H, M = map(int, input().split())
    hour_angle = (H * 60 + M) * 0.5
    minute_angle = M * 6
    angle = abs(hour_angle - minute_angle)
    if angle > 180:
        angle = 360 - angle
    angle = math.radians(angle)
    print(math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(angle)))

if __name__ == '__main__':
    main()
