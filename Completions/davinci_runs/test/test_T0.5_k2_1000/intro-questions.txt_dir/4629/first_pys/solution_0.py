

# SOLUTION

import sys

def main():
    q = int(sys.stdin.readline())
    for i in range(q):
        n = int(sys.stdin.readline())
        m = 1
        while m < n:
            m *= 3
        print(m)

if __name__ == "__main__":
    main()