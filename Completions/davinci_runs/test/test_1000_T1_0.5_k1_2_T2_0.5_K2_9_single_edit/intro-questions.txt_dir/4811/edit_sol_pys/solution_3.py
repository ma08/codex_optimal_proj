
import sys

def main():
    k = int(sys.stdin.readline().strip())
    n = 1
    while 2**n <= k:
        n *= 2
    print(n, n)

if __name__ == '__main__':
    main()
