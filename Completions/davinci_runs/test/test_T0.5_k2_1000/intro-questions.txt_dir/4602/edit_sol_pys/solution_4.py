
import sys

def get_line():
    return list(map(int, sys.stdin.readline().rstrip().split(' ')))

def main():
    N = get_line()[0]
    K = get_line()[0]
    xs = get_line()
    min_distance = 0
    for x in xs:
        min_distance += min(x, K - x) * 2
    print(min_distance)

if __name__ == '__main__':
    main()
