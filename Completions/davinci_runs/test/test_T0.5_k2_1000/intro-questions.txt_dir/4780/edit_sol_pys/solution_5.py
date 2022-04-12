


def main():
    """Ants."""
    num_1, num_2, time = map(int, input().split())
    row_1, row_2 = input(), input()
    for _ in range(time):
        for i in range(min(num_1, num_2)):
            row_1[i], row_2[i] = row_2[i], row_1[i]  # swap
    print(row_1)
    print(row_2)

if __name__ == "__main__":
    main()
