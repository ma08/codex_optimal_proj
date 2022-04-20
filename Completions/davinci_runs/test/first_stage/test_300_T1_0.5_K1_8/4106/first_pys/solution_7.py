

import sys

def main():
    n, k, x = [int(i) for i in sys.stdin.readline().split()]
    arr = [int(i) for i in sys.stdin.readline().split()]
    if x < k:
        print(-1)
        return
    if x == n:
        print(sum(arr))
        return
    arr.sort()
    print(sum(arr[n-x:]))

if __name__ == "__main__":
    main()