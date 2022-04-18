
import math

def main():
    x1, y1 = input().split()
    x1, y1 = int(x1), int(y1)
    x2, y2 = input().split()
    x2, y2 = int(x2), int(y2)
    x3, y3 = input().split()
    x3, y3 = int(x3), int(y3)
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    s = (a + b + c) / 2.0
    print(math.sqrt(s * (s - a) * (s - b) * (s - c)) * 100)

if __name__ == "__main__":
    main()
