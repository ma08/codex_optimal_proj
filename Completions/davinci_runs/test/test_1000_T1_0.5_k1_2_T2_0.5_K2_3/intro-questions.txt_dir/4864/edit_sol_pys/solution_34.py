
import sys

# read input
R, C, ZR, ZC = map(int, sys.stdin.readline().split())
article = []
for _ in range(R):
    article.append([s for s in sys.stdin.readline().rstrip()])

# enlarge the article
enlarged_article = []
for row in article:
    enlarged_row = []
    for c in row:
    enlarged_article.extend([enlarged_row] * ZR)

# print the enlarged article
for row in enlarged_article:
    print(''.join(row))
