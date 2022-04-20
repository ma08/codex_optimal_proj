import sys

def main():
    p, q, r = map(int, sys.stdin.readline().split())
    print(min(p + q, p + r, q + r))

if __name__ == '__main__':
    main()
