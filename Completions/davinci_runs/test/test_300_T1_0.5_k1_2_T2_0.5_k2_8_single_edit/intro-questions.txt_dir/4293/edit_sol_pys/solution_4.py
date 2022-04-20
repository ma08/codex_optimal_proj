

import sys

def main():
    A, B, C = map(int, input().split())
    print(min(A+B, B+C, C+A))

if __name__ == "__main__":
    main()
