

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
    falcon = []
    for i in range(n):
        for j in range(m*2):
            if image[i][j] == char:
                falcon.append((i,j))

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
