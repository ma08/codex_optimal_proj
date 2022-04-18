import math


def main():
    a, b = map(float, input().split())
    c, d = map(float, input().split())
    t = float(input())

    if math.sqrt((a - c) ** 2 + (b - d) ** 2) <= t:
        print("Y")
    else:
        print("N")

main()
