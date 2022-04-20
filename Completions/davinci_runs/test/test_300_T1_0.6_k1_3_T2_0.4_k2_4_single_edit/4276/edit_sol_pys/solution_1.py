

import sys

def main():
    N, T = map(int, input().split())
    routes = sorted([(c, t) for c, t in [map(int, input().split()) for _ in range(N)]])
    print(routes[0][0] if routes[0][1] <= T else 'TLE')

if __name__ == '__main__':
    main()
