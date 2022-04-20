

import math

def main():
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    arr.reverse()
    print(find(n,m,arr))

def find(n,m,arr):
    sum = 0
    for i in range(m):
        sum += arr[i]
    return sum
    

if __name__ == '__main__':
    main()
