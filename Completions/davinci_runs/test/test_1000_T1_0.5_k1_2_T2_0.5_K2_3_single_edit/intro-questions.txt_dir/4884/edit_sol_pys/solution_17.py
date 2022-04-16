import sys

def main():
    carrots = 0
    n, p = map(int, sys.stdin.readline().split()) # read two integers
    for i in range(n):
        sys.stdin.readline() # read a line
        carrots += p
    print carrots

if __name__ == '__main__':
    main()
