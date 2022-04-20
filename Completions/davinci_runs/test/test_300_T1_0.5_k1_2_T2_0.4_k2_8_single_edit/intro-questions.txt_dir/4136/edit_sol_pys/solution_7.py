import math


def main():
    a, b, h, m = map(int, input().split())
    theta_h = (h * 30 + m * 0.5) * math.pi / 180
    theta_m = (m * 6) * math.pi / 180
    theta = abs(theta_h - theta_m)
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(theta))
    print(c)

main()
