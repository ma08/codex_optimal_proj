
import sys

def main():
    N = int(input())
    K = int(input())
    xs = list(map(int, input().split()))
    min_dist = 0
    for x in xs:
        min_dist += min(x, K - x) * 2
    print(min_dist)

if __name__ == '__main__':
    main()
