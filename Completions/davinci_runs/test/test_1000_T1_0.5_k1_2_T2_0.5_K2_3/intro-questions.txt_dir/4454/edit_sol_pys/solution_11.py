# Code


def min_price(arr: list) -> int:
    total = sum(arr)  # O(n)
    max_val = max(arr)  # O(n)
    if (total - max_val) >= max_val:  # O(1)
        return max_val  # O(1)
    return total // len(arr)  # O(1)


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        arr = list(map(int, input().split()))
        print(min_price(arr))
