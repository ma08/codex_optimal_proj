
import sys

def main():
    k = int(sys.stdin.readline().strip())
    n = 0
    while 2**n < k:
        n += 1
    print(2**n)

if __name__ == '__main__':
    main()
