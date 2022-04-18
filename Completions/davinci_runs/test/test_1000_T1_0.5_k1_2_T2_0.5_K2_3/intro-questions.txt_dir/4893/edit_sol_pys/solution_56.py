

def main():
    n, p = map(int, input().split())
    distances = [int(input()) for _ in range(n)]
    distances.sort()
    print(min(distances[i] - distances[i-1] for i in range(1, n)))


if __name__ == '__main__':
    main()
