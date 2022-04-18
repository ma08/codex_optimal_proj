# testing


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * n
    i = 0
    j = n - 1
    for k in range(n):
        if k % 2 == 0:
            b[k] = a[j]
            j -= 1
        else:
            b[k] = a[i]
            i += 1
    print(*b, sep='\n')


if __name__ == '__main__':
    main()
