
def min_moves(a, b):
    if a > b:
        return min_moves(b, a)

    if a == b:
        return 0

    max_delta = 10
    min_delta = max(1, b - (a + max_delta))

    return 1 + min(min_moves(a + delta, b) for delta in range(min_delta, max_delta + 1))


if __name__ == '__main__':
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        a, b = map(int, input().split())
        print(min_moves(a, b))
