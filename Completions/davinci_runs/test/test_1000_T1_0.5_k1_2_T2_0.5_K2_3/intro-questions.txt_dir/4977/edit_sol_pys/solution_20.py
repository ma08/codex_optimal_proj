import math

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    t = int(input())

    if math.sqrt((a - c) ** 2 + (b - d) ** 2) <= t:
        print("Y")
    else:
        print("N")

main()
