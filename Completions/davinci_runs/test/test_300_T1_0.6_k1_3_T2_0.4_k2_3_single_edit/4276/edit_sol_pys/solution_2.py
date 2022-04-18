
import sys

def main():
    N, T = map(int, input().split())
    routes = []
    for i in range(N):
        c, t = map(int, input().split())
        routes.append((c, t))
    routes.sort()
    for c, t in routes:
        if t <= T:
            print(c)
            return
    print('TLE')

if __name__ == '__main__':
    main()
