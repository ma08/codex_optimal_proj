

import sys

def main():
    N = int(input())
    count = 0
    i = 1
    while True:
        if N == 1:
            break
        if N%2 == 0:
            N = N // 2
        else:
            N = N - 1
        count += 1
    print(count)

if __name__ == '__main__':
    main()