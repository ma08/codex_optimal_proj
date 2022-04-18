
import sys

def main():
    # read input
    n, m, char = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    char = char[1]
    image = ['']*n
    for i in range(n):
        image[i] = sys.stdin.readline().rstrip()
    sys.stdin.readline() # empty line
    for i in range(n):
        image[i] += sys.stdin.readline().rstrip()

    # find the falcon
    falcon = set()
    for i in range(n):
        for j in range(m*2):
            if image[i][j] == char:
                falcon.add((i,j))

    # find the leftmost and rightmost points
    # the points are needed to be able to calculate the center of the falcon
    left = m
    right = 0
    for i in falcon:
        if i[1] < left:
            left = i[1]
        if i[1] > right:
            right = i[1]

    # calculate the center of the falcon
    center = (0, left + (right - left)//2)

    # find the topmost and bottommost points
    # the points are needed to be able to calculate the vertical shift
    top = n
    bottom = 0
    for i in falcon:
        if i[0] < top:
            top = i[0]
        if i[0] > bottom:
            bottom = i[0]

    # calculate the vertical shift
    shift = (bottom - top)//2

    # create the result image
    result = ['']*(n+shift)
    for i in range(n):
        result[i] = image[i][:m]

    # shift the falcon vertically
    for i in falcon:
        result[i[0]+shift][i[1]-m] = char

    # shift the falcon horizontally
    for i in falcon:
        result[i[0]+shift][i[1]-m+1] = char

    # print the result
    for i in range(n):
        print(result[i])
    print()

if __name__ == '__main__':
    main()
