
print(r, c, zr, zc)
r, c, zr, zc = map(int, input().split())

article = []
for i in range(r):
    article.append(input())

for i in range(r):
    for j in range(c):
        for k in range(zr):
            for l in range(zc):
                print(article[i][j], end="")
        print()
