

import sys

def readline():
    return sys.stdin.readline().strip()

def main():
    n = int(readline())
    names = []
    for i in range(n):
        names.append(readline())

    for i in range(len(names)):
        print(names[i])

if __name__ == '__main__':
    main()
