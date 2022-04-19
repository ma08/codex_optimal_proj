
import sys

def main():
    a, b = map(int, sys.stdin.readline().split())  # read a line with a space
    print(a - b)  # print the result

if __name__ == "__main__":
    main()
