

import sys

def main():
    # Read the input
    N = int(input())
    ratings = [int(x) for x in input().split()]

    # Find the minimum and maximum number of colors
    minColors = 0
    maxColors = 0
    ratingColors = [False]*8
    for rating in ratings:
        if rating >= 3200:
            maxColors += 1
        else:
            color = rating // 400
            if ratingColors[color] == False:
                ratingColors[color] = 1
                minColors += 1
    if minColors == 0:
        minColors = 1
    print(minColors, maxColors)

if __name__ == '__main__':
    main()
