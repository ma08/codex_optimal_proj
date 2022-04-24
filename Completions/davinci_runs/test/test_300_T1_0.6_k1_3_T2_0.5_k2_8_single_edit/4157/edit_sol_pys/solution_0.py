

from math import log, floor

def solve(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if arr[i] % 3 == 0:
            arr[i] = arr[i] // 3
            if i > 0 and arr[i] == arr[i - 1]:
                arr.pop(i - 1)
    for i in range(n - 1):
        if arr[i] != arr[i + 1] * 2:
            return False
    return True

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if not solve(arr):
        arr.reverse()
        if not solve(arr):
            print("No")
            return
    print(*arr)

if __name__ == '__main__':
    main()
