def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        elif h[i] < h[i - 1]:
            count += 1
            h[i] = h[i - 1]
    print(count)


if __name__ == '__main__':
    main()
