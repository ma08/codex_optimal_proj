

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 2:
        print(2)
        return

    max_length = 0
    length = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            length += 1
            max_length = max(max_length, length)
        else:
            length = 1
    print(max_length)


if __name__ == "__main__":
    main()