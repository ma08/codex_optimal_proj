

from math import sqrt, ceil

def main():
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    if k == 0:
        print(max(arr))
        exit()
    arr.sort()
    ans = arr[-1]
    for i in range(n):
        if arr[i] == 0:
            print(0)
            exit()
        ans = max(ans, ceil(arr[i + k] / arr[i]))
    print(ans)

if __name__ == "__main__":
    main()
