

import sys

def main():
    n = int(input())
    if (n % 2 == 0):
        print("Alice")
        print(n // 2 - 1)
    else:
        print("Bob")

if __name__ == "__main__":
    main()
