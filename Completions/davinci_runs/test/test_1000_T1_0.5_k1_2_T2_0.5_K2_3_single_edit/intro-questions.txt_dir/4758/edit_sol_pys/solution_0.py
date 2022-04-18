

import sys

def main():
    N,T,M = map(int,sys.stdin.readline().split())
    print(N*T*M//8)

if __name__ == "__main__":
    main()
