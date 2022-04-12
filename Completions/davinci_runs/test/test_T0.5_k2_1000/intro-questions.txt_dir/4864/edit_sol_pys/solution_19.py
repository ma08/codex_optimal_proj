# Read input
r, c, zr, zc = [int(x) for x in input().split()]
article = [input() for _ in range(r)]

# Enlarge article and print
for row in article:
    for _ in range(zr):
        print(row.replace(".", "..").replace("X", "XX"))
