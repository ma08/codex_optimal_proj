


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]

    max_instability = 0
    for i in range(n):
        instability = max(arr[:i] + arr[i + 1:]) - min(arr[:i] + arr[i + 1:])
        if instability > max_instability:
            max_instability = instability

    print(max_instability)


if __name__ == "__main__":
    main()