
def solve(n, m, arr):
    """
    :param n: Number of elements in the array
    :param m: Value of the median
    :param arr: Array of values
    :return: Number of indices that have the median equal to m
    """
    count = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i:j + 1] == [m] * (j - i + 1):
                count += 1

    return count


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(solve(n, m, arr))
