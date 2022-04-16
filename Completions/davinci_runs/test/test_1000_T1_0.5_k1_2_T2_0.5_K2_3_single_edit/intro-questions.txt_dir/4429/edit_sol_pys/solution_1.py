

import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        x, y = map(int, sys.stdin.readline().split())
        if x == y:
            print("YES")
            print(x, y)
        else:
            print("NO")

if __name__ == "__main__":
    main()
