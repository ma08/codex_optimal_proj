


def main():
    n, V = map(int, input().split())
    box_volumes = []
    for _ in range(n):
        box_volumes.append(int(input().split()[0]) * int(input().split()[1]) * int(input().split()[2]))
    print(max(box_volumes) - V)


if __name__ == "__main__":
    main()
