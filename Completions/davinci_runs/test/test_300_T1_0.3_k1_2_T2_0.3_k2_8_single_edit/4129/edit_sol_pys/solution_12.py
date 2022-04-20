
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        print(arr[b-1] - arr[a-1])

main()
