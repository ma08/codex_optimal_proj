
def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [i for i in range(len(a))]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                b[i], b[j] = b[j], b[i]
    print(*b)


if __name__ == '__main__':
    main()
