

def main():
    n = int(input())  # number of rows
    m = int(input())  # number of columns
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    # print(matrix)
    # print(n, m)
    # for row in matrix:
    #     print(row)
    for row in matrix:
        for i in range(len(row)):
            if i == 0:
                print(row[i], end=" ")
            elif i == len(row)-1:
                print(row[i])
            else:
                print(row[i], end=" ")

main()
