import sys
sys.setrecursionlimit(10000000)
from collections import deque

def main():
    n = int(input())
    arr = []
    for i in range(n): arr.append(int(input()))
    arr.sort()
    arr = list(dict.fromkeys(arr))
    print(len(arr))
    print(*arr)

main()
