
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    res = [r]
    for line in sys.stdin:
        a, b = map(int, line.split())
        if a > res[-1]:
            res.append(res[-1])
        else:
            res.append(max(res[-1] - b, 0))
    print(len(res) - 1)

if __name__ == "__main__":
    main()
