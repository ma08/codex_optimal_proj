

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    print(sum(i for i in range(1, n+1) if i%3 and i%5))

if __name__ == '__main__':
    main()