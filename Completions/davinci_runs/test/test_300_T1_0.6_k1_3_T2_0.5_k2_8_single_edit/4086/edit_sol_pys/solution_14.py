def main():
    n = int(input())
    a = list(map(int, input().split()))
    unique = []
    for i in range(n-1, -1, -1):
        if a[i] not in unique:
            unique.append(a[i])
    print(len(unique))
    print(*unique[::-1])


if __name__ == '__main__':
    main()
