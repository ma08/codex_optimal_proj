


def main():
    n, r = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    # print(a)
    # print(b)

    for i in range(n):
        if r < a[i]:
            print("NO")
            break
        r += b[i]
        if r < 0:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    main()