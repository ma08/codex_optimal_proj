

def main(m, n, u, l, r, d):  # m = rows, n = columns, u = up, l = left, r = right, d = down
    out = ""
    for i in range(u):
        out += "#." * (l + n + r) + "#\n"
    for i in range(m):
        out += "#." + ".".join(input().split()) + ".#\n"
    for i in range(d):
        out += "#." * (l + n + r) + "#\n"
    print(out)

if __name__ == "__main__":
    m, n = map(int, input().split())
    u, l, r, d = map(int, input().split())
    main(m, n, u, l, r, d)
