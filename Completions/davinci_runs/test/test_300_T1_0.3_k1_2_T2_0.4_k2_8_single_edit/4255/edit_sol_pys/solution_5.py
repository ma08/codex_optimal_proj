


import math

def get_area(a, b, c):
    s = (a + b + c) / 2

    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def main():
    a, b, c = map(int, input().split())
    print(int(get_area(a, b, c)))

if __name__ == '__main__':
    main()
