
import sys

def read_input():
    line = sys.stdin.readline().strip()
    return [i for i in line]

def main():
    print(read_input())

if __name__ == "__main__":
    main()
