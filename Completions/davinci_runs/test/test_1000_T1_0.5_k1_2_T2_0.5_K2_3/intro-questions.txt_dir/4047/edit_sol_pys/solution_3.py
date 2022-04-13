

import sys

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if n % 2 == 0:
        print(arr[n//2] - arr[n//2 - 1] + 1)
    else:
        print(0)

if __name__ == "__main__":
    main()
