
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    r = [0]
    d = 0
    for line in sys.stdin:
        a, b = map(int, line.split())
        if a > r[-1]:
            r.append(r[-1] + b)
        else:
            d = max(d, r[-1] - b)
    print(d)

if __name__ == "__main__":
    main()
