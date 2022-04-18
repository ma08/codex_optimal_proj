
import sys

def calc_min_fare(a, b, c, d, e, f):
    return min(a, b) + min(c, d) + min(e, f)

def main():
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    d = int(sys.stdin.readline())
    print(calc_min_fare(a, b, c, d))

if __name__ == '__main__':
    main()
