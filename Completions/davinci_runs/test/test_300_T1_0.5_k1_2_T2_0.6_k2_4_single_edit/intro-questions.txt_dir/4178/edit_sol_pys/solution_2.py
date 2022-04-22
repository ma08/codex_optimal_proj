

def is_ascending(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            return False
    return True


def increment(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            array[i] += 1



def main():
    n = int(input())
    heights = list(map(int, input().split()))

    increment(heights)

    print('Yes' if is_ascending(heights) else 'No')


if __name__ == '__main__':
    main()
