


def main():
    n = int(input())
    a = list(map(int, input()))
    f = list(map(int, input().split()))

    max_num = []
    for i in range(n):
        max_num.append(f[a[i]-1])

    max_num_str = ''.join(map(str, max_num))
    print(max_num_str)


if __name__ == '__main__':
    main()