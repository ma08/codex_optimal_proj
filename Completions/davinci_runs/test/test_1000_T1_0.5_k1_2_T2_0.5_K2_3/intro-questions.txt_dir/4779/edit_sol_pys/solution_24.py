
import math
import sys

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    sum_sq = 0
    sum_lin = 0 
    for i in range(n):
        if i < (n//2):
            sum_sq += math.pow(a[i],2)
        else:
            sum_lin += a[i]
    print(int(sum_sq*sum_lin))

if __name__ == '__main__':
    main()
