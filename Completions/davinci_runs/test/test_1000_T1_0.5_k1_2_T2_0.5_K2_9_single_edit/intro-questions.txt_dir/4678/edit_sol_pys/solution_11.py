
import sys

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    print(arr)
    prev = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] != prev:
            count += 1
            prev = arr[i]
    print(count)

main()
