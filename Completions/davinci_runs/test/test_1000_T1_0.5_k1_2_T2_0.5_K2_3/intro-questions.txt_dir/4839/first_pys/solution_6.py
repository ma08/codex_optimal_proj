

import sys

def main():
    n = int(sys.stdin.readline())
    cans = [int(x) for x in sys.stdin.readline().split()]
    cans.sort()
    cans.reverse()
    if cans[0] > n:
        print("impossible")
    else:
        print(float(cans[n-1])/n)

if __name__ == '__main__':
    main()