

import sys

def main():
    a, b = sys.stdin.readline().strip().split()
    for i in range(len(a)):
        if a[i] in b:
            print(a)
            print(b)
            return
    print("No match")

if __name__ == "__main__":
    main()
