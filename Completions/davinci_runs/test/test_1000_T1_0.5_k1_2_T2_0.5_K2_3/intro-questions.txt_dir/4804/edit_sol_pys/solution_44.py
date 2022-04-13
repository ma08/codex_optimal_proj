
import sys

def main():
    n = int(sys.stdin.readline())
    print("%d:" %n)
    for i in range(2, n):
        if (n % i == 0) and ((n // i)>1):
            print("%d,%d" %(i, n // i))

if __name__ == '__main__':
    main()
