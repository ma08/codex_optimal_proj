

import sys
readline = sys.stdin.buffer.readline

def main():
    n = int(readline())    
    print(2 ** (n - 1).bit_length())

if __name__ == '__main__':
    main()
