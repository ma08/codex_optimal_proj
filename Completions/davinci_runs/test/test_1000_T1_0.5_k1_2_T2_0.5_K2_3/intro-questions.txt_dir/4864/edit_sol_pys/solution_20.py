

def read_input():
    r, c, zr, zc = [int(x) for x in input().split()]
    article = [input() for _ in range(r)]  # noqa: E741
    return r, c, zr, zc, article


def enlarge_article(article, zr):
    for row in article:
        for _ in range(zr):
            print(row.replace(".", "..").replace("x", "xx"))


def main():
    r, c, zr, zc, article = read_input()
    enlarge_article(article, zr)  # noqa: E741


if __name__ == "__main__":
    main()
