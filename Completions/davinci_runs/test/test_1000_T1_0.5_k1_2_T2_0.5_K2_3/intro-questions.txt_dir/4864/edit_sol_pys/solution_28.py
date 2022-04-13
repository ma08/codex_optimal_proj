

r, c, zr, zc = map(int, input().split()) # r = rows, c = columns, zr = zoom rows, zc = zoom columns

article = []
for i in range(r):
    article.append(list(input()))

for i in range(r):
    for j in range(zr):
        for k in range(zc):
            for l in range(c):
                print(article[i][l], end="")
            print()
