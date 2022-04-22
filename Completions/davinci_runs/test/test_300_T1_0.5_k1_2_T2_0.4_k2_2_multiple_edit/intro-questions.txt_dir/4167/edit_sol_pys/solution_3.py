
# from math import pow
import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    ans = 0
    for i in range(1,k+1):
        if i <= n:
            ans += n - i + 1
    
    print(pow(ans,3),end='')

if __name__ == '__main__':
    main()
