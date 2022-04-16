

import sys

def main():
    a, b = sys.stdin.readline().strip().split()
    for i in range(len(a)):
        if a[i] in b:
            for j in range(i):
                print('.' * len(b))
            print(b)
            for j in range(i+1, len(a)):
                print('.' * len(b))
            break

if __name__ == "__main__":
    main()
