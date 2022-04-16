


def main():
    t = int(input())
    for _ in range(t):
        b = input()
        n = len(b)
        a = b[0]
        for i in range(1, n):
            if b[i] == a[0]:
                a = b[i] + a
            elif b[i] == a[-1]:
                a = a + b[i]
        print(a)


if __name__ == '__main__':
    main()