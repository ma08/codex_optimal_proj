import os

import sys

def main():
    with open('file.txt', 'r') as f:
        for line in f:
            x = float(line)
            a = int(round(x, 0))
            b = int(round(x * 10, 0)) - a * 10
            print(a, b)

if __name__ == '__main__':
    main()
