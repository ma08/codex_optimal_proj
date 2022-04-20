

def ravioli_sort(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) >= 2:
            return False
    return True


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if ravioli_sort(arr) else "NO")


if __name__ == "__main__":
    main()
