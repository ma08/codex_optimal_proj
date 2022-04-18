

def main():
    # Read the input
    N = int(input())
    ratings = [int(x) for x in input().split()]

    # Find the minimum and maximum number of colors
    minColors = 0
    maxColors = 0
    ratingColors = [None]*8
    for r in ratings:
        if r >= 3200:
            maxColors += 1
        elif ratingColors[r // 400] is None:
            ratingColors[r // 400] = 1
            minColors += 1
    print(minColors or 1, minColors + maxColors)

if __name__ == '__main__':
    main()
