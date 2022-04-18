
r, c, zr, zc = map(int, input().split())  # r=row, c=column, zr=zoom in row, zc=zoom in column

article = []  # article is the list of the string
for i in range(r):
    article.append(input())  # read from input and append it to the list

for i in range(r):
    for j in range(zr):  # zoom in row
        for k in range(c):  # looping through the row
            for l in range(zc):  # zoom in column
                print(article[i][k], end="")  # print the string
        print()
