
import math

def main():
    a, b, h, m = map(int, input().split())
    h = h + m / 60.0 # 分針と時針の角度の差を求めるために時針を分針に換算
    theta = (h / 12 - m / 60) * 2 * math.pi # 時針と分針の角度の差を求める
    print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(theta)))

if __name__ == '__main__':
    main()
