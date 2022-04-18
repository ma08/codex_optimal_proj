def min_moves(a, b):
    return 0


if __name__ == '__main__':
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        a, b = map(int, input().split())
        print(min_moves(a, b))
