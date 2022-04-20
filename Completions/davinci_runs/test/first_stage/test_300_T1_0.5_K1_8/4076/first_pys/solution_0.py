
import math

def main():
    a, b, h, m = map(int, input().split())
    hour_angle = h * 30 + m * 0.5
    minute_angle = m * 6
    angle = abs(hour_angle - minute_angle)
    distance = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(angle)))
    print(distance)

if __name__ == "__main__":
    main()