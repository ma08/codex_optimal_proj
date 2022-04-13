import sys

def get_line():
    return list(map(int, sys.stdin.readline().strip().split()))

def main():
    n, k = get_line()
    xs = get_line()[:n]
    min_distance = 0
    for x in xs:
        min_distance += min(x, k - x) * 2
    print(min_distance)

if __name__ == '__main__':
    main()
