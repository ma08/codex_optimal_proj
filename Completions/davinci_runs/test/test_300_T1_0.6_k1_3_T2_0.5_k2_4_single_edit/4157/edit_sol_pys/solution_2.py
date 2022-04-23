

from math import log, floor

def solve(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
            j = i - 1
            while j >= 0 and arr[i] != arr[j]:
                j -= 1
            arr.pop(j)
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
