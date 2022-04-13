
import sys

def check(n, L, H):
    n = str(n)
    if len(set(n)) != 6:
        return False
    else:
        for i in n:
            if int(L) % int(i) != 0:
                return False
            else:
                return True

def main():
    L, H = map(int, sys.stdin.readline().split())
    count = 0
    for i in range(L, H+1):
        if check(i, L, H):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
