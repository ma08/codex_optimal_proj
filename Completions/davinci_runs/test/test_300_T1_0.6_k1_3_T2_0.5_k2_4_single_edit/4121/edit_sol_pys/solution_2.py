

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # print(a)
    # print(b)
    # print(n, m)

    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                print(a[i], end=' ')
            else:
                print('0', end=' ')
        print()


if __name__ == "__main__":
    main()
