
import sys

def isHarshard(n):
    n = str(n)
    return int(n) % sum([int(i) for i in n]) == 0

def nextHarshard(n):
    n += 1
    while not isHarshard(n):
        n += 1
    return n

def main():
    n = int(sys.stdin.readline())
    print(nextHarshard(n))

if __name__ == "__main__":
    main()
