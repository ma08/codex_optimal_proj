
import math

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    if sum(arr) == 0:
        print(-1)
        return

    if arr[0] > 0:
        print(n - 1)
        return

    if arr[0] < 0:
        print(n - 1)
        return

    if arr[0] == 0:
        print(n)
        return

    return


if __name__ == "__main__":
    main()
