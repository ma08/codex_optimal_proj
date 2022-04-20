

import sys

def main():
    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    
    d = {}
    for i in range(n):
        d[a[i]] = i+1
    d = sorted(d.items())
    
    for k, v in d:
        print(v)
        
if __name__ == '__main__':
    main()