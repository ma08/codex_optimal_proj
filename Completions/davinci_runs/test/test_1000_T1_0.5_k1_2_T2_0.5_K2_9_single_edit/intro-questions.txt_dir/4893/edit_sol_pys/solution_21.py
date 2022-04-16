


def main():
    n, p = map(int, input().split())
    distances = list(map(int, input().split()))
    distances.sort()
    print(min([distances[i] - distances[i-1] for i in range(p, n)]))


if __name__ == '__main__':
    main()
