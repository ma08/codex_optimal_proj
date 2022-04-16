

import sys

def main():
    s = sys.stdin.readline().rstrip().split()
    s = [x.replace("<", "") for x in s]
    print(s)

if __name__ == "__main__":
    main()
