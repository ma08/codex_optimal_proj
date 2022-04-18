import math


def main():
    h, v = map(int, input().split())
    print(int(round(h / math.sin(math.radians(v)))))

if __name__ == "__main__":
    main()
