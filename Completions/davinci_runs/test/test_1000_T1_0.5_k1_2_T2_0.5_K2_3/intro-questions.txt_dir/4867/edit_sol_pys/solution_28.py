

def main(h, w, u, l, r, d):
    out = ""
    for i in range(u):
        out += "#." * (l + w + r) + "#\n"
    for i in range(h):
        out += "#." + ".".join(input()) + ".#\n"
    for i in range(d):
        out += "#." * (l + w + r) + "#\n"
    print(out)

if __name__ == "__main__":
    h, w = map(int, input().split())
    u, l, r, d = map(int, input().split())
    main(h, w, u, l, r, d)
