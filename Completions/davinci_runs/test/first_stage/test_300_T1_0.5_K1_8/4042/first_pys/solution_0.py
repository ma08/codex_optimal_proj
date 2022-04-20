

import sys

def main():
    x = float(sys.stdin.readline())
    a = int(x)
    b = int(round((x-a)*10))

    print(a, b)

if __name__ == "__main__":
    main()