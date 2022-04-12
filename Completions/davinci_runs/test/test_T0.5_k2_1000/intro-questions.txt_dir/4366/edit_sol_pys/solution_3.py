

import sys

def main():
    line = sys.stdin.readline()
    a,b = line.split()
    a = int(a)
    b = int(b)
    print((a+b)%24) 

if __name__ == '__main__':
    main()
