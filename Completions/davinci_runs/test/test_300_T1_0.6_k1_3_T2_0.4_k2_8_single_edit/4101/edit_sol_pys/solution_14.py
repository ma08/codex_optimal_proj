
import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()] # n = rows, m = columns

    a = [] # a = matrix
    for i in range(n):
        a.append([int(x) for x in sys.stdin.readline().split()])

    r = [0]*n # r = row
    c = [0]*m # c = column

    for i in range(n):
        zero = 0 # zero = number of 0s in a row
        one = 0 # one = number of 1s in a row
        for j in range(m):
            if a[i][j] == 0:
                zero += 1
            else:
                one += 1
        if zero > one: # if there are more 0s in a row than 1s, then the row is flipped
            r[i] = 1

    for j in range(m):
        zero = 0 # zero = number of 0s in a column
        one = 0 # one = number of 1s in a column
        for i in range(n):
            if a[i][j] == 0:
                zero += 1
            else:
                one += 1
        if zero > one: # if there are more 0s in a column than 1s, then the column is flipped
            c[j] = 1

    for i in range(n):
        for j in range(m):
            if r[i] == 1: # if the row is flipped, then the elements in the row are flipped
                a[i][j] = 1 - a[i][j]
            if c[j] == 1: # if the column is flipped, then the elements in the column are flipped
                a[i][j] = 1 - a[i][j]

    sorted = True # sorted = true if the matrix is sorted, false otherwise
    for i in range(n):
        for j in range(m-1):
            if a[i][j] > a[i][j+1]: # if the current element is greater than the next element, then the matrix is not sorted
                sorted = False

    if sorted:
        print("YES")
        print("".join([str(x) for x in r]))
        print("".join([str(x) for x in c]))
    else:
        print("NO")

if __name__ == '__main__':
    main()
