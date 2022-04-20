

import sys

def main():
    n = int(input())
    s = input()
    print("YES")
    for i in range(n):
        print(i % 2, end='')

if __name__ == "__main__":
    main()
