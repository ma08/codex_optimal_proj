
import sys

def main():
    for line in sys.stdin:
        x, k, d = map(int, line.rstrip().split())
        if abs(x) < k * d:
            print(abs(x - (x // d) * d))
        else:
            print(abs(x) - (k * d))

if __name__ == '__main__':
    main()
