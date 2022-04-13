
import sys

def check(n):
    n = str(n)
    if len(set(n)) != 6:
        return False
    for i in range(10):
        if (int(n) % (i+1)) != 0:
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
