

import sys

def main():
    a = int(sys.stdin.readline().strip())
    b = int(sys.stdin.readline().strip())
    c = int(sys.stdin.readline().strip())
    d = int(sys.stdin.readline().strip())
    print(int(not(a or b or c or d)))

if __name__ == '__main__':
    main()
