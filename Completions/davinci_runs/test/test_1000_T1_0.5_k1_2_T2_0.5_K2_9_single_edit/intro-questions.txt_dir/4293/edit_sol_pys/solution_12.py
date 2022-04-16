

import sys

def main():
    P, Q, R = map(int, sys.stdin.readline().split())
    print(min(P+Q, Q+R, R+P))

if __name__ == "__main__":
    main()
