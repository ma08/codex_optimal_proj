
import sys

def main():
    for line in sys.stdin.readlines():
        n, shuffle = line.strip().split()
        n = int(n)

        if shuffle == 'out':
            print(n//2)
        else:
            print(n-1)

if __name__ == '__main__':
    main()
