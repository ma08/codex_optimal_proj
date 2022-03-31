

def main():
    n, m = [int(x) for x in input().split()] # n - rows, m - columns
    matrix = []
    for i in range(n): # read matrix
        matrix.append([int(x) for x in input().split()]) # matrix[i][j] - element in i-th row and j-th column

    rows = [0] * n # rows[i] - number of 1s in i-th row
    columns = [0] * m # columns[j] - number of 1s in j-th column
    for i in range(n): # count number of 1s in each row and column
        for j in range(m): # matrix[i][j] - element in i-th row and j-th column
            if matrix[i][j] == 1: # if element is 1
                rows[i] += 1 # increase number of 1s in i-th row
                columns[j] += 1 # increase number of 1s in j-th column

    for i in range(n): # check if it is possible to change matrix
        for j in range(m): # matrix[i][j] - element in i-th row and j-th column
            if (rows[i] + columns[j]) % 2 != matrix[i][j]: # if it is impossible to change element in i-th row and j-th column
                print("NO") # print "NO"
                return # finish program
    print("YES") # print "YES"
    print(" ".join(["1" if x % 2 == 1 else "0" for x in rows])) # print new rows
    print(" ".join(["1" if x % 2 == 1 else "0" for x in columns])) # print new columns

if __name__ == "__main__":
    main()
