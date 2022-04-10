

import sys

def main():
    a,b,c = map(int,sys.stdin.readline().split())
    print(min(a,b,c)*7+min(a,b,c)-max(a,b,c))

if __name__ == "__main__":
    main()