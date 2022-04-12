
import sys

def isHarshad(n): # isHarshad is a function that checks if the number is Harshad
    n = str(n)
    return int(n) % sum([int(i) for i in n]) == 0

def nextHarshad(n): # nextHarshad is a function that finds the next Harshad number
    n += 1
    while not isHarshad(n):
        n += 1
    return n

def main():
    n = int(sys.stdin.readline()) # read the input
    print(nextHarshad(n))

if __name__ == "__main__":
    main()
