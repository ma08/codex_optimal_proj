
r, c, zr, zc = map(int, input().split())

article = []
for i in range(r):
    article.append(input())

for i in range(r*zr):
    for j in range(c*zc):
        print(article[i//zr][j//zc], end="")
    print()
