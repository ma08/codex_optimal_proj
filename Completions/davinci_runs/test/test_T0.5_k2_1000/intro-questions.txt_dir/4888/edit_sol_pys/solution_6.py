import sys

def main():
    n, T = map(int, input().split())
    times = map(int, input().split())
    acc = 0
    for i in range(n):
        acc += times[i]
        if acc > T:
            print i
            return
    print n

if __name__ == '__main__':
    main()
