

from math import pi, cos, sin

def get_answer(A, B, H, M):
    hour_angle = (H + M / 60) * (360 / 12) * (pi / 180)
    minute_angle = M * (360 / 60) * (pi / 180)

    x1 = A * cos(hour_angle)
    y1 = A * sin(hour_angle)
    x2 = B * cos(minute_angle)
    y2 = B * sin(minute_angle)
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def main():
    A, B, H, M = map(int, input().split())
    print("{:.20f}".format(get_answer(A, B, H, M)))

if __name__ == '__main__':
    main()