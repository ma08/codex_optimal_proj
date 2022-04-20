

from math import log, floor

def solve(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] // 3
    return arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr = solve(arr)
    print(*arr)

if __name__ == '__main__':
    main()
