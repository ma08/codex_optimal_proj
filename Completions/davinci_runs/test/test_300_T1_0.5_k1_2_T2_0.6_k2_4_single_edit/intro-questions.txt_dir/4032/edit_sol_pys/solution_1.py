


def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 1:
        print("No")
    else:
        mid_idx = n // 2
        if a[:mid_idx] == a[mid_idx:]:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
