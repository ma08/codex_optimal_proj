
#
import sys

#read input
R, C, ZR, ZC = map(int, sys.stdin.readline().split())
article = []
for _ in range(R):
    article.append([s for s in sys.stdin.readline().rstrip()])

#enlarge article
enlarged = []
for row in article:
    enlarged_row = []
    for c in row:
        enlarged_row.extend([c]*ZC)
    enlarged.extend([enlarged_row]*ZR)

#print enlarged article
for row in enlarged:
    print(''.join(row))
