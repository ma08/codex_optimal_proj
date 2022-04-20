#!/usr/bin/env python3


from itertools import accumulate

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    b = [list(map(int, input().split())) for i in range(m)]
    for i in range(n-m+1):
        for j in range(n-m+1):
            for k in range(m):
                for l in range(m):
                    if a[i+k][j+l] != b[k][l]:
                        break
                else:
                    continue
                break
            else:
                print('Yes')
                sys.exit()
    print('No')

if __name__ == "__main__":
    main()
