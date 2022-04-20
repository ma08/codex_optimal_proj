import sys

def main():
    n = int(sys.stdin.readline())
    x = [int(i) for i in sys.stdin.readline().split()]
    x.sort()
    m = x[0]
    for i in range(1, n):
        m = (m + x[i]) / 2
    print(sum([(i - m) ** 2 for i in x]))

if __name__ == '__main__':
    main()
