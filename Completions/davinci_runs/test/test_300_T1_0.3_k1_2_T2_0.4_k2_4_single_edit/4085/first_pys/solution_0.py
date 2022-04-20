


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = list(map(int, input().split()))
        divisors.sort()
        if divisors[0] == 2:
            print(2 * divisors[-1])
        else:
            print(-1)


if __name__ == "__main__":
    main()