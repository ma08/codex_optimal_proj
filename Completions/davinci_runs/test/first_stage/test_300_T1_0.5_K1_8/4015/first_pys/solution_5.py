

import sys

def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

def main():
    n, m = read_ints()
    count = 0
    if n == m:
        print(count)
    else:
        while n < m:
            if m % 2 == 0:
                m /= 2
                count += 1
            elif m % 3 == 0:
                m /= 3
                count += 1
            else:
                print(-1)
                return
        while n > m:
            if n % 2 == 0:
                n /= 2
                count += 1
            elif n % 3 == 0:
                n /= 3
                count += 1
            else:
                print(-1)
                return
        print(count)

if __name__ == '__main__':
    main()