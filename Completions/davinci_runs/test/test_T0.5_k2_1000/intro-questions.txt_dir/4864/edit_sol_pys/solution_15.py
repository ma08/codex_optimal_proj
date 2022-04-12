

# Read input
r, c, zr, zc = [int(x) for x in input().split()] # r = rows, c = columns, zr = row zoom, zc = column zoom
article = [input() for _ in range(r)] # article = article

# Enlarge the article
for row in article:
    for _ in range(zr):
        print(row.replace(".", "..").replace("x", "xx"))
