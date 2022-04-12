
import sys
import math

def main():
    line = sys.stdin.readline().strip()
    if line == '0':
        print('0')
    else:
        print(int(line) + 1)

if __name__ == '__main__':
    main()
