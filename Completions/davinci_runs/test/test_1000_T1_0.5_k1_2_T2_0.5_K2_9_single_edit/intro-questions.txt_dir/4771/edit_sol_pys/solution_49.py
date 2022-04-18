


def main():
    n, V = map(int, input().split())
    box_volumes = [int(input().split()[0]) * int(input().split()[1]) * int(input().split()[2]) for _ in range(n)]
    print(max(box_volumes) - V) if max(box_volumes) > V else print("KO")


if __name__ == "__main__":
    main()
