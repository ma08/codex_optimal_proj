

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
    return min(abs(s-b), abs(ceil(s/ingredients[0][0])-b+ingredients[0][1]), abs(floor(s/ingredients[0][0])-b+ingredients[0][1]))

n = int(stdin.readline())
ingredients = []
for i in range(n):
    s, b = map(int, stdin.readline().split())
    ingredients.append([s, b])
print(main(n, ingredients))
