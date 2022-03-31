
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)

    num_pockets = 1
    current_pocket = a[0] - 1
    for i in range(1, n):
        if a[i] > current_pocket:
            num_pockets += 1 
            current_pocket = a[i]

    print(num_pockets)


if __name__ == "__main__":
    main()
