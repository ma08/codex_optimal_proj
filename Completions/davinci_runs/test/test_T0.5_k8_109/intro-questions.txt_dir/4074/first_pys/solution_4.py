

import sys

def main():
    cases = int(sys.stdin.readline())
    for i in range(cases):
        line = sys.stdin.readline().split()
        n = int(line[0])
        k = int(line[1])
        print(n//k + (1 if n%k != 0 else 0))

if __name__ == "__main__":
    main()