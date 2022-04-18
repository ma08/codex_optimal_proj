def main():
    n = int(input())
    h = list(map(int, input().split()))

    for i in range(1, n):
        if h[i - 1] > h[i]:
            h[i] += 1

    for i in range(1, n):
        if h[i - 1] > h[i]:
            print('No')
            break
    else:
        print('Yes')


if __name__ == '__main__':
    main()
