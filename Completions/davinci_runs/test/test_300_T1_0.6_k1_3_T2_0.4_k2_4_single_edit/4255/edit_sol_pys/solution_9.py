
import math

def main():
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    s = (a + b + c) / 2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(area)

if __name__ == "__main__":
    main()
