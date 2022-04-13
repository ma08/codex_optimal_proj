
import sys

def main():
    # Read the input
    N = int(input())
    ratings = [int(x) for x in input().split()]

    # Find the minimum and maximum number of colours
    minColours = 0
    maxColours = 0
    ratingColours = [None]*8
    for rating in ratings:
        if rating >= 3200:
            maxColours += 1
        else:
            colour = rating // 400
            if ratingColours[colour] == None:
                ratingColours[colour] = 1
                minColours += 1
    if minColours == 0:
        minColours = 1
    print(minColours, maxColours)

if __name__ == '__main__':
    main()
