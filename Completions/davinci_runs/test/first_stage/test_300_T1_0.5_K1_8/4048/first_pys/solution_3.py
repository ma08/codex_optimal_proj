

import sys

def main():
    n = int(sys.stdin.readline())
    i = 1
    j = 1
    count = 0
    while True:
        if i == n or j == n:
            print(count)
            break
        if i < j:
            i += 1
        else:
            j += 1
        count += 1

if __name__ == '__main__':
    main()