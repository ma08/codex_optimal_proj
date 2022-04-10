

import sys

def main():
    k = int(sys.stdin.readline())
    n = 7
    cnt = 1
    while True:
        if n % k == 0:
            print(cnt)
            break
        n = n * 10 + 7
        cnt += 1

if __name__ == '__main__':
    main()