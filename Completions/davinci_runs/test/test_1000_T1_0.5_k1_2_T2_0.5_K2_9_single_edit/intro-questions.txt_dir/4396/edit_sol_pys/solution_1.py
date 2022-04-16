

import sys

def main():
    N = int(sys.stdin.readline())
    sum = 0
    for i in range(N):
        x, u = sys.stdin.readline().split()
        x = float(x)
        if u == 'JPY':
            sum += x
        elif u == 'BTC':
            sum += x * 380000.0
    print(sum)

if __name__ == '__main__':
    main()
