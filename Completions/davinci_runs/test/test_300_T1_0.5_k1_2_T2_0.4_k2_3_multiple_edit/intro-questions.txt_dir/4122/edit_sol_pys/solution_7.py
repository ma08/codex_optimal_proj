
import math

def main():
    h, n = map(int, input().split())
    arr = list(map(int, input().split()))

    if sum(arr) <= h:
        print(-1)
        return

    count = 0
    for i in range(n):
        count += math.ceil(h / arr[i])

    print(count)
    return


if __name__ == "__main__":
    main()
