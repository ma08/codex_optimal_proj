

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = []
    for i in range(n):
        a.append(int(sys.stdin.readline().strip()))
    a.sort()
    sum_sq = 0
    sum_lin = 0
    for i in range(n):
        if i < (n//2):
            sum_sq += a[i]**2
        else:
            sum_lin += a[i]
    print(sum_sq*sum_lin)

    return

if __name__ == '__main__':
    main()
