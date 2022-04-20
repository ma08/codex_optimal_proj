
import sys

def main():
    d, n = map(int, sys.stdin.readline().split()) # read input
    if d == 0:
        print(n) # print output
    elif d == 1:
        print(100 * n) # print output
    else:
        print(10000 * n) # print output

if __name__ == '__main__':
    main()
