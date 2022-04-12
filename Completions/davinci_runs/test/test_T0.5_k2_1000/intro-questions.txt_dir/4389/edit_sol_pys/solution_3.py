
def main():
    t = int(input())
    for _ in range(t):
        b = input()
        n = len(b)
        a = ''
        a += b[0]
        for i in range(1, n):
            if b[i] == a[0]:
                a = a + b[i]
            elif b[i] == a[-1]:
                a = b[i] + a
        print(a)


if __name__ == '__main__':
    main()
