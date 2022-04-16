

import sys

def main():
    # read input
    n, m, char = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    char = char[0]
    image = ['']*n
    for i in range(n):
        image[i] = sys.stdin.readline().rstrip()
    sys.stdin.readline() # empty line
    for i in range(n):
        image[i] += sys.stdin.readline().rstrip()

    # find the falcon
    falcon = []
    for i in range(n):
        for j in range(m*2):
            if image[i][j] == char:
                falcon.append((i,j))

    # find the leftmost and rightmost points
    # the points are needed to be able to calculate the center of the falcon
    left = falcon[0]
    right = falcon[0]
    for i in range(1, len(falcon)):
        if falcon[i][1] < left[1]:
            left = falcon[i]
        if falcon[i][1] > right[1]:
            right = falcon[i]

    # calculate the center of the falcon
    center = (left[0], left[1] + (right[1] - left[1])//2)

    # find the topmost and bottommost points
    # the points are needed to be able to calculate the vertical shift
    top = falcon[0]
    bottom = falcon[0]
    for i in range(1, len(falcon)):
        if falcon[i][0] < top[0]:
            top = falcon[i]
        if falcon[i][0] > bottom[0]:
            bottom = falcon[i]

    # calculate the vertical shift
    shift = (bottom[0] - top[0])//2

    # create the result image
    result = ['']*n
    for i in range(n):
        result[i] = image[i][:m]

    # shift the falcon vertically
    for i in range(len(falcon)):
        result[falcon[i][0]][falcon[i][1]-m] = char

    # shift the falcon horizontally
    for i in range(len(falcon)):
        result[falcon[i][0]][falcon[i][1]-m+1] = char

    # print the result
    for i in range(n):
        print(result[i])
    print()

if __name__ == '__main__':
    main()
