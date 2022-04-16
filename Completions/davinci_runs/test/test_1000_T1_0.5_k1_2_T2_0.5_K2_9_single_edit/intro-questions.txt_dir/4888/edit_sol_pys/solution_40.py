import sys

def main():
    n, T = map(int, sys.stdin.readline().split())
    times = map(int, sys.stdin.readline().split())
    acc = 0
    for i in range(n):
        acc += times[i]
        if acc > T:
            print i
            return
    print n

if __name__ == '__main__':
    main()
