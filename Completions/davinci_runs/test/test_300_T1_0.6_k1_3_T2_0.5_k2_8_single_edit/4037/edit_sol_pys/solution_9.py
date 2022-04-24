
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    r = [r] * n
    for line in sys.stdin:
        a, b = map(int, line.split()) # a is the time of the next event, b is the cost
        r[a-1] = max(r[a-1] - b, 0)
    print(sum(r))

if __name__ == "__main__":
    main()
