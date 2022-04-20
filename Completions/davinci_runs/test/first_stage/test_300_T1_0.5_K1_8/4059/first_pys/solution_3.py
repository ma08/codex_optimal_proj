

import sys

def main():
    N = int(sys.stdin.readline())
    # print(N)
    count = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            c = N - a*b
            if c > 0:
                count += 1
    print(count)

if __name__ == "__main__":
    main()