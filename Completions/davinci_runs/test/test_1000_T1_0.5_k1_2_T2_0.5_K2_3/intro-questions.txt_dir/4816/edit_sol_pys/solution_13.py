
import math

def main():
    x, y, x1, y1, x2, y2 = [int(x) for x in input().split()]

    # check if the goat can reach the house from the top or left side
    if x < x1:
        # check if the goat can reach the house from the top right corner
        if y > y2:
            distance = math.sqrt((x-x1)**2 + (y-y2)**2)
        # check if the goat can reach the house from the top left corner
        else:
            distance = math.sqrt((x-x1)**2 + (y-y1)**2)
    # check if the goat can reach the house from the bottom or right side
    else:
        # check if the goat can reach the house from the bottom left corner
        if y < y1:
            distance = math.sqrt((x-x2)**2 + (y-y1)**2)
        # check if the goat can reach the house from the bottom right corner
        else:
            distance = math.sqrt((x-x2)**2 + (y-y2)**2)

    print(distance)

if __name__ == '__main__':
    main()
