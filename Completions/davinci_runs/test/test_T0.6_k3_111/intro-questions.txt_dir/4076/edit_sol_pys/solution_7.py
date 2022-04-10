
import math

def main():
    a, b, h, m = map(int, input().split())
    h = h + m / 60
    theta = (h / 12 - m / 60) * 2 * math.pi
    print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(theta)))

if __name__ == '__main__':
    main()
