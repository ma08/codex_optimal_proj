


def print_article(article, r, c, zr, zc):
    for i in range(r):
        for j in range(zr):
            for k in range(c):
                for l in range(zc):
                    print(article[i][k], end="")
            print()

r, c, zr, zc = map(int, input().split())

article = []
for i in range(r):
    article.append(input())

print_article(article, r, c, zr, zc)
