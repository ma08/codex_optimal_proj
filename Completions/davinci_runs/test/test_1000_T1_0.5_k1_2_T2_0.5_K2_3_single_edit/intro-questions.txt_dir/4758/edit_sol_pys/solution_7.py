import sys

import sys

def main():
    n, t, m = [int(i) for i in sys.stdin.readline().split()] # read a line with a single integer
    print(n * t * m) # print the result

if __name__ == "__main__":
    main()
