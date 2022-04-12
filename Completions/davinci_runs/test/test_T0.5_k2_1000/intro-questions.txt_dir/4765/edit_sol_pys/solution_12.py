

from sys import stdin
from math import ceil
from math import floor

def main(n, ingredients):
    # if n == 1:
    #     return ingredients[0][1] - ingredients[0][0]
    # else:
    #     s = ingredients[0][0]
    #     b = ingredients[0][1]
    #     for i in range(1,n):
    #         s *= ingredients[i][0]
    #         b += ingredients[i][1]
    #     return abs(s - b)
    s = 1
    b = 0
    for i in range(n):
        s *= ingredients[i][0]
        b += ingredients[i][1]
    return min(abs(s-b), abs(ceil(s/ingredients[0][0])-b+ingredients[0][1]), abs(floor(s/ingredients[0][0])-b+ingredients[0][1]), abs(ceil(s/ingredients[1][0])-b+ingredients[1][1]), abs(floor(s/ingredients[1][0])-b+ingredients[1][1]), abs(ceil(s/ingredients[2][0])-b+ingredients[2][1]), abs(floor(s/ingredients[2][0])-b+ingredients[2][1]), abs(ceil(s/ingredients[3][0])-b+ingredients[3][1]), abs(floor(s/ingredients[3][0])-b+ingredients[3][1]), abs(ceil(s/ingredients[4][0])-b+ingredients[4][1]), abs(floor(s/ingredients[4][0])-b+ingredients[4][1]), abs(ceil(s/ingredients[5][0])-b+ingredients[5][1]), abs(floor(s/ingredients[5][0])-b+ingredients[5][1]), abs(ceil(s/ingredients[6][0])-b+ingredients[6][1]), abs(floor(s/ingredients[6][0])-b+ingredients[6][1]), abs(ceil(s/ingredients[7][0])-b+ingredients[7][1]), abs(floor(s/ingredients[7][0])-b+ingredients[7][1]), abs(ceil(s/ingredients[8][0])-b+ingredients[8][1]), abs(floor(s/ingredients[8][0])-b+ingredients[8][1]), abs(ceil(s/ingredients[9][0])-b+ingredients[9][1]), abs(floor(s/ingredients[9][0])-b+ingredients[9][1]), abs(ceil(s/ingredients[10][0])-b+ingredients[10][1]), abs(floor(s/ingredients[10][0])-b+ingredients[10][1]), abs(ceil(s/ingredients[11][0])-b+ingredients[11][1]), abs(floor(s/ingredients[11][0])-b+ingredients[11][1]), abs(ceil(s/ingredients[12][0])-b+ingredients[12][1]), abs(floor(s/ingredients[12][0])-b+ingredients[12][1]), abs(ceil(s/ingredients[13][0])-b+ingredients[13][1]), abs(floor(s/ingredients[13][0])-b+ingredients[13][1]), abs(ceil(s/ingredients[14][0])-b+ingredients[14][1]), abs(floor(s/ingredients[14][0])-b+ingredients[14][1]), abs(ceil(s/ingredients[15][0])-b+ingredients[15][1]), abs(floor(s/ingredients[15][0])-b+ingredients[15][1]), abs(ceil(s/ingredients[16][0])-b+ingredients[16][1]), abs(floor(s/ingredients[16][0])-b+ingredients[16][1]), abs(ceil(s/ingredients[17][0])-b+ingredients[17][1]), abs(floor(s/ingredients[17][0])-b+ingredients[17][1]), abs(ceil(s/ingredients[18][0])-b+ingredients[18][1]), abs(floor(s/ingredients[18][0])-b+ingredients[18][1]), abs(ceil(s/ingredients[19][0])-b+ingredients[19][1]), abs(floor(s/ingredients[19][0])-b+ingredients[19][1]))

n = int(stdin.readline())
ingredients = []
for i in range(n):
    s, b = map(int, stdin.readline().split())
    ingredients.append([s, b])
print(main(n, ingredients))
