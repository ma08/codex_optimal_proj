

import sys

def main():    
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr = sorted(arr)
    print(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                arr.pop(j)
                n -= 1
                j -= 1
    print(arr)
    print(n)

if __name__ == '__main__':
    main()
