
def main():
    n, p = map(int, input().split())
    distances = list(map(int, input().split()))
    distances.sort()
    print(min([distances[i] - distances[i-1] for i in range(1, n)]))  # noqa: E501


if __name__ == '__main__':
    main()
