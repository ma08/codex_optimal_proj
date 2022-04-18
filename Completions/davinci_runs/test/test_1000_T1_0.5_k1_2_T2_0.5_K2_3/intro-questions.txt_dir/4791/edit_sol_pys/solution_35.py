from math import sqrt


def area(a, b, c):
    s = (a + b + c) / 2
    return sqrt((s - a) * (s - b) * (s - c))

def main():
    s = [int(x) for x in input().split()]
    s.sort()
    print(max(area(s[0], s[1], s[2]), area(s[0], s[1], s[0] + s[1])))


if __name__ == "__main__":
    main()
