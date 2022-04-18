

def main(m, n, u, l, r, d):
    print("#." * (l + n + r) + "#" * (u + 1))
    for i in range(u + m + d):
        if i < u:
            print("#." * (l + n + r) + "#")
        elif i < u + m:
            print("#." + ".".join(input()) + ".#")
        else:
            print("#." * (l + n + r) + "#")


if __name__ == "__main__":
    m, n = map(int, input().split())
    u, l, r, d = map(int, input().split())
    main(m, n, u, l, r, d)
