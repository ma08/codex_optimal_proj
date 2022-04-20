import numpy as np

import sys

def main():
    a, b = map(int, input().split())

    for i in range(10000):
        if int(i * 1.08) == a:
            if int(i * 1.1) == b:
                print(i)
                sys.exit()
    print(":(")

if __name__ == '__main__':
    main()
