

import sys

def isHarshad(n):
    n = str(n)
    return int(n) % sum([int(i) for i in n]) == 0

def nextHarshad(n):
    n += 1
    while not isHarshad(n):
        n += 1
    return n

def main():
    n = int(sys.stdin.readline().strip())
    print(nextHarshad(n))

if __name__ == "__main__":
    main()
