import sys

def isHarshad(n):
    return n % sum([int(i) for i in str(n)]) == 0

def nextHarshad(n):
    n += 1
    while not isHarshad(n):
        n += 1
    return n

def main():
    n = int(sys.stdin.readline())
    print(nextHarshad(n))

if __name__ == "__main__":
    main()
