#!/usr/bin/env python3

def read_input():
    r, c, zr, zc = [int(x) for x in input().split()]
    article = [input() for _ in range(r)]
    return r, c, zr, zc, article


def enlarge_article(article, zr):
    for row in article:
        for _ in range(zr):
            print(row.replace(".", "..").replace("X", "XX"))


def main():
    r, c, zr, zc, article = read_input()
    enlarge_article(article, zr)


if __name__ == "__main__":
    main()
