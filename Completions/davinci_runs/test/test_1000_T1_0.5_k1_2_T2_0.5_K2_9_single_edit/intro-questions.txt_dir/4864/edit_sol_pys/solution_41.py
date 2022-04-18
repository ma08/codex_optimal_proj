

r, c, zr, zc = map(int, input().split())

article = []
for i in range(r):
    article.append(list(input()))

for i in range(r):
    for j in range(zr):
        for k in range(c):
            for l in range(zc):
                print(article[i][k], end="")  # end="" is to prevent from new line
        print()  # new line
