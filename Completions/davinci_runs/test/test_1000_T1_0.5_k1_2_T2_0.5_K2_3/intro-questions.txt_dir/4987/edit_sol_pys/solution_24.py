


def binary_search(arr, x):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            return m
        if arr[m] < x:
            l = m + 1
        else:
            r = m - 1

    return -1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    for i in range(m):
        x = int(input())
        print(binary_search(a, x))


if __name__ == "__main__":
    main()
