
def concat(a, b):
    length = len(str(a))
    return a * 10 ** length + b


    """
    Returns the number of iterations it takes to get to 6174
    """
def kaprekar(n):
    n = str(n)
    n1 = int(''.join(sorted(n)))
    n2 = int(''.join(sorted(n)[::-1]))
    if n2 == n1:
        return 0
    return 1 + kaprekar(n2 - n1)


def is_divisible(a, b, k):
    return concat(a, b) % k == 0


    """
    Returns the number of pairs of numbers in arr that are divisible by k
    """
def solve(n, k, arr):
    count = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if is_divisible(arr[i], arr[j], k):
                count += 1
            j += 1
        i += 1
    return count


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))


if __name__ == "__main__":
    main()
