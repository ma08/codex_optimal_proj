import math

def main():
    a, b, h, m = map(int, input().split())
    hour_angle = 30*h + 30*m/60
    min_angle = 6*m
    theta = abs(hour_angle-min_angle)
    ans = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta)))
    print(ans)

if __name__ == "__main__":
    main()
