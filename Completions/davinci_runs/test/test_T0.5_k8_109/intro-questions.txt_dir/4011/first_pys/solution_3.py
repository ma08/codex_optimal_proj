


def solve(n, a, f):
    # a = list(map(int, a))
    # f = list(map(int, f.split()))
    f = [0] + f
    # print(a)
    # print(f)

    a = list(a)
    for i in range(n):
        a[i] = f[int(a[i])]
    # print(a)

    cnt = 1
    i = n - 1
    while i > 0:
        if a[i] > a[i-1]:
            break
        i -= 1
    # print(i)
    if i > 0:
        a[i-1] = f[int(a[i-1])]
        cnt += 1
    # print(a)
    a = ''.join(map(str, a))
    return a, cnt


def main():
    n = int(input())
    a = input()
    f = input()
    a, cnt = solve(n, a, f)
    print(a)
    # print(cnt)


if __name__ == '__main__':
    main()