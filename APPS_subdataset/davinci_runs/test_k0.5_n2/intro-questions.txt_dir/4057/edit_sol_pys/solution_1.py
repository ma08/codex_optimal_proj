
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    num_pockets = 0
    current_pocket = 0
    for i in range(1, n):
        if a[i] > current_pocket:
            num_pockets += 1
            current_pocket = a[i]

    print(num_pockets)


if __name__ == "__main__":
    main()
