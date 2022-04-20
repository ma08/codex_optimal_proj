#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This program shows the area and perimeter of a rectangle
#    with user input


def main():
    # this function shows the area and perimeter of a rectangle
    # input
    length = int(input("Enter length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm): "))
    # process
    area = length*width
    perimeter = 2*(length+width)
    # output
    print("")
    print("Area is {}mm^2".format(area))
    print("Perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
