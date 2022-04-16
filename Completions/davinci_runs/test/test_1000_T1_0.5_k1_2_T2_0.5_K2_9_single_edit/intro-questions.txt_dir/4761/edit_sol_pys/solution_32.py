

import sys

def check(n):
    num = str(n)
    if len(set(num)) != 6:
        return False
    for i in num:
        if int(num) % int(i) != 0:
            return False
    return True

def main():
    L, H = map(int, sys.stdin.readline().split())
    count = 0
    for i in range(L, H+1):
        if check(i):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
