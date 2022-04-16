

def main(m, n, u, l, r, d):
    out = []
    for i in range(u):
        out.append("#." * (l + n + r) + "#\n")
    for i in range(m):
        out.append("#." + ".".join(input()) + ".#\n")
    for i in range(d):
        out.append("#." * (l + n + r) + "#\n")
    print("".join(out))

if __name__ == "__main__":
    m, n = map(int, input().split())
    u, l, r, d = map(int, input().split())
    main(m, n, u, l, r, d)
