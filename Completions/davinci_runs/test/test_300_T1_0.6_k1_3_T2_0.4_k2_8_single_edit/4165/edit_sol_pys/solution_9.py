
import sys

def main():
    n = int(sys.stdin.readline())
    lengths = list(map(int, sys.stdin.readline().split())) #list of all lengths
    if max(lengths) < sum(lengths) - max(lengths): #if the max length is less than the total length minus the max length, then it's possible
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
