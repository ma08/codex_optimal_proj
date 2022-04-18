
import math

def main():
    x, y, x1, y1, x2, y2 = [int(x) for x in input().split()]  # input coordinates

    # check if the goat can reach the house from the top or left side
    if x < x1:
        # check if the goat can reach the house from the top side (y2)
        if y > y2:
            distance = math.sqrt((x-x1)**2 + (y-y2)**2)
        # check if the goat can reach the house from the left side (y1)
        else:
            distance = math.sqrt((x-x1)**2 + (y-y1)**2)
    # check if the goat can reach the house from the bottom or right side
    else:
        # check if the goat can reach the house from the bottom side (y1)
        if y < y1:
            distance = math.sqrt((x-x2)**2 + (y-y1)**2)
        # check if the goat can reach the house from the right side (y2)
        else:
            distance = math.sqrt((x-x2)**2 + (y-y2)**2)

    print(distance)

if __name__ == '__main__':
    main()
