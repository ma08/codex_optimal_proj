

import sys

def main():
    N = int(sys.stdin.readline().strip())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                print("Yes")
                return
    print("No")

if __name__ == "__main__":
    main()