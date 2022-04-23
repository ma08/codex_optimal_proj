

def main():
    # Read input and initialize variables
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    count = 0

    # Count the number of pairs that are in the wrong order
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j] and b[i] < b[j]:
                count += 1
            elif a[i] < a[j] and b[i] > b[j]:
                count += 1

    # Output
    print(count)


if __name__ == "__main__":
    main()
