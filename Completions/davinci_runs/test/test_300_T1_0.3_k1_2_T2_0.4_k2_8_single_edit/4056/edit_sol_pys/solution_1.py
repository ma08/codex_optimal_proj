
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))[:n]
    print(sum(a))

if __name__ == '__main__':
    main()
