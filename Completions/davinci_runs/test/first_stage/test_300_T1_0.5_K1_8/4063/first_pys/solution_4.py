

#import numpy as np
#import scipy as sp

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    cnt = 0
    for i in range(N):
        if d[i] == d[N//2-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()