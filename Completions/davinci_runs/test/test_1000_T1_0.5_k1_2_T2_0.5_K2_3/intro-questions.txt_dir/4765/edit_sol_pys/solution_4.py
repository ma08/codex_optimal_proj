

from math import sqrt
from sys import stdin
from math import ceil
from math import floor

def main(n, ingredients, d):
    s = 1.0
    b = 0.0
    for i in range(n-1):
        s *= ingredients[i][0]
        b += ingredients[i][1]
    s = round(s, d)
    b = round(b, d)
    minimum = abs(s-b)
    for i in range(n-1):
        s = round(s/ingredients[i][0], d)
        b = round(b-ingredients[i][1], d)
        minimum = min(minimum, abs(s-b))
        s = round(s*ingredients[i][0], d)
        b = round(b+ingredients[i][1], d)
    return minimum

n = int(stdin.readline())
ingredients = []
for i in range(n):
    s, b = map(int, stdin.readline().split())
    ingredients.append([s, b])
print(main(n, ingredients, 5))
