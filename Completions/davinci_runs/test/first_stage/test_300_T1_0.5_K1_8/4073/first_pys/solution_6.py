

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = sys.stdin.readline().strip().split()
    a = [int(i) for i in a]
    a.sort()
    if n == 1:
        print(1)
        return
    if a[0] == 1:
        print(1)
        return
    # print(a)
    max = a[-1]
    for i in range(n):
        if a[i] > i + 1:
            print(i + 2)
            return
    print(max + 1)

if __name__ == '__main__':
    main()