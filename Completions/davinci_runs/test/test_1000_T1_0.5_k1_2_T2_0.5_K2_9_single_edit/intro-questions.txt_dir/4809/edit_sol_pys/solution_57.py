

def main():
    s, n = map(int, input().split())
    print(coconut_splat(s, n))


def coconut_splat(s, n, l):
    if len(l) == n:
        return l
    else:
        for i in range(2, n + 1):
            if s % i == 1:
                l.append(i)
                coconut_splat(s * i, n, l)
                l.pop()


if __name__ == "__main__":
    main()
