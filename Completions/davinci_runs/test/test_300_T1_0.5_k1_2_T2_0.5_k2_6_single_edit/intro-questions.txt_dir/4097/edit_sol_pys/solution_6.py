
import sys

def main():
    num = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    for i in arr:
        print(i, end=" ")

if __name__ == "__main__":
    main()
