import math

def main():
    a, b, c = [int(x) for x in input().split()]
    s = (a + b + c) / 2.0
    print(math.sqrt(s * (s - a) * (s - b) * (s - c)))  # s * (s - a) * (s - b) * (s - c) is the area of the triangle

if __name__ == "__main__":
    main()
