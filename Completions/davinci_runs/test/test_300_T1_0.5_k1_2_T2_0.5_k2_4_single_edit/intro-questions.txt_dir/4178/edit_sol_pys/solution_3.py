


def is_ascending(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def main():
    n = int(input())
    heights = [int(i) for i in input().split()]

    print('Yes' if is_ascending(heights) else 'No')


if __name__ == '__main__':
    main()
