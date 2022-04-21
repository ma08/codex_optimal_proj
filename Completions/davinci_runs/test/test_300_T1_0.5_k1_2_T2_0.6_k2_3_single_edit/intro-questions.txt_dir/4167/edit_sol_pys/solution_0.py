

import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    ans = []
    for i in range(1,k):
        if i <= n and (n-i) % k == 0:
            ans.append(i)
    
    print(ans**3)

if __name__ == '__main__':
    main()
