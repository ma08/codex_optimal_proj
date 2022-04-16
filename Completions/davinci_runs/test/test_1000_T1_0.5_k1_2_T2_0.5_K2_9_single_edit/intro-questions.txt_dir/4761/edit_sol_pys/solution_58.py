
import sys

def check(n):
    n_str = str(n)
    if len(set(n_str)) != 6:
        return False
    for i in n_str:
        if int(n_str) % int(i) != 0:
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
