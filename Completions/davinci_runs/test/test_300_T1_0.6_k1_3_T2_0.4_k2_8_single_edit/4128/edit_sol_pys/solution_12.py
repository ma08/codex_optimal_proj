
#!/bin/python3


import sys


def find_max_sum(arr):
    n = len(arr)
    max_sum = -sys.maxsize
    for i in range(n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j+1):
                curr_sum += arr[k]
            max_sum = max(max_sum, curr_sum)
    return max_sum


    sys.setrecursionlimit(10**6)
def main():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        print(find_max_sum(arr))


if __name__ == '__main__':
    main()
