

import math

def solve(a, b, h, m):
    """ solve the problem """

    # calculate the angle
    h_angle = (h + m / 60) * 30
    m_angle = m * 6

    # calculate the distance
    angle = abs(h_angle - m_angle)
    angle = min(angle, 360 - angle)
    return math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle)))

def main():
    """ main function """
    a, b, h, m = map(int, input().split())
    print(solve(a, b, h, m))

if __name__ == '__main__':
    main()