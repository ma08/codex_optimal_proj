

import sys

def main():
    data = sys.stdin.readline()
    while data:
        print(len(data))
        data = sys.stdin.readline()

if __name__ == "__main__":
    main()
