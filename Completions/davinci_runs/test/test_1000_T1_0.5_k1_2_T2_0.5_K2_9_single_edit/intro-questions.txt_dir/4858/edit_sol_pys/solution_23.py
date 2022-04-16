

import sys

def main():
    n, m, char = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    char = char[1]
    image = ['' for i in range(n)]
    for i in range(n):
        image[i] = sys.stdin.readline().rstrip()
    sys.stdin.readline()
    for i in range(n):
        image[i] += sys.stdin.readline().rstrip()

    falcon = []
    for i in range(n):
        for j in range(m*2):
            if image[i][j] == char:
                falcon.append((i,j))

    left = falcon[0]
    right = falcon[0]
    for i in range(1, len(falcon)):
        if falcon[i][1] < left[1]:
            left = falcon[i]
        if falcon[i][1] > right[1]:
            right = falcon[i]

    center = (left[0], left[1] + (right[1] - left[1])//2)

    top = falcon[0]
    bottom = falcon[0]
    for i in range(1, len(falcon)):
        if falcon[i][0] < top[0]:
            top = falcon[i]
        if falcon[i][0] > bottom[0]:
            bottom = falcon[i]

    shift = (bottom[0] - top[0])//2

    result = ['' for i in range(n)]
    for i in range(n):
        result[i] = image[i][:m]

    for i in range(len(falcon)):
        result[falcon[i][0]][falcon[i][1]-m] = char

    for i in range(len(falcon)):
        result[falcon[i][0]][falcon[i][1]-m+1] = char

    for i in range(n):
        print(result[i])
    print()

if __name__ == '__main__':
    main()
