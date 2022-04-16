

import sys

def main():
    with open(sys.stdin.readline().strip()) as f:
        print(len(f.readlines()))

if __name__ == "__main__":
    main()
