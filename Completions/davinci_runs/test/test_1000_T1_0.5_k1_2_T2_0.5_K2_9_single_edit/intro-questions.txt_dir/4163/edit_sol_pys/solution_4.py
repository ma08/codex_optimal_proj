

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    D = []
    for i in range(N):
        D.append(list(map(int, sys.stdin.readline().rstrip().split())))
    print(D)
    return

if __name__ == "__main__":
    main()
