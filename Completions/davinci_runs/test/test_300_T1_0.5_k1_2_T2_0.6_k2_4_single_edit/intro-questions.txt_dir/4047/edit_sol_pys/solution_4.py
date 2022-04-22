

import sys

def main():
    a, b = map(int, input().split())
    if a * b % 2 == 0:
        print("Even")
    elif a * b % 2 == 1:
        print("Odd")

if __name__ == "__main__":
    main()
