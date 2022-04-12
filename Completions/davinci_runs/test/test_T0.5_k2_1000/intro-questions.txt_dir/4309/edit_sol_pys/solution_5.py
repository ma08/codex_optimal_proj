

import sys

def main():
    N = int(sys.stdin.readline().strip())
    for i in range(N, 1000):
        if (i % 111) == 0:
            print(i)
            break

if __name__ == "__main__":
    main()
